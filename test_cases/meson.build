
test_hdr = join_paths(meson.source_root(), 'export', 'test.h')
extrn_hdr = join_paths(meson.source_root(), 'export', 'other_module.h')
cffi_build = cffi_tool.process( test_hdr, extra_args:['_pi_test', extrn_hdr])

cffi_lib = shared_library('_pi_test', 
            sources:cffi_build, 
            link_with:[c_code],
            link_args:[python_exe.get_variable('BLDLIBRARY')],
            include_directories:[python_exe.get_variable('INCLUDEPY')],
            native: true,
            name_prefix: '')


fs = import('fs')
test1 = fs.copyfile(files('test_run.py'), 'test_run.py')

test('test_sample', python_exe, args: ['-m','pytest', '-s', 'test_run.py'], 
                depends : [cffi_lib, test1],
                workdir: meson.current_build_dir())
