from cffi import FFI
import sys

if len(sys.argv) != 5:
    raise RuntimeError("Requires two arguments")

header_file = sys.argv[1]
build_file_path = sys.argv[2]
module_name = sys.argv[3]
external_hdr = sys.argv[4]

ffibuilder = FFI()

with open(external_hdr) as fr:
    ehdr = fr.read()
    ffibuilder.embedding_api(ehdr)

with open(header_file) as fr:
    c_hdr = fr.read()
    ffibuilder.cdef(c_hdr)

ffibuilder.set_source(module_name,
    source="""
        #include "%s"
    """%(header_file))

if __name__ == "__main__":
    # ffibuilder.compile(module_name, verbose=True)
    ffibuilder.emit_c_code(build_file_path)

