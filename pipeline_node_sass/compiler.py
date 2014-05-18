from pipeline.compilers import SubProcessCompiler
from django.utils.encoding import smart_bytes
from pipeline.conf import settings
from os.path import dirname

class NodeSassCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        command = "{} {} {}".format(
            getattr(settings, 'PIPELINE_NODE_SASS_BINARY', '/usr/bin/env node-sass'),
            getattr(settings, 'PIPELINE_NODE_SASS_ARGUMENTS', '--output-style compressed'),
            infile
        )

        return self.execute_command(command, cwd=dirname(infile))


    def execute_command(self, command, content=None, cwd=None):
        """
        Due to node-sass writing to stderr even when rendering CSS properly, simply show messages.
        """
        import subprocess
        pipe = subprocess.Popen(command, shell=True, cwd=cwd,
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if content: 
            content = smart_bytes(content)
        stdout, stderr = pipe.communicate(content)

        if self.verbose or stderr.strip():
            print(stderr)

        return stdout
