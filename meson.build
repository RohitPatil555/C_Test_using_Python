
project('cffi_ex01', 'c')

c_code_src = []

subdir('src')

c_code = static_library('c_code', c_code_src,
                 native: true,
                 include_directories:['export'],)

pymod = import('python')
python_exe = pymod.find_installation() 

cffi_script = join_paths(meson.source_root(), 'build_tools', 'generate_cffi_code.py')

cffi_tool = generator(
    python_exe,
    arguments: [ cffi_script, '@INPUT@', join_paths('@BUILD_DIR@','cffi_@BASENAME@.c'), '@EXTRA_ARGS@'],
    output: 'cffi_@BASENAME@.c'
)

subdir('test_cases')

