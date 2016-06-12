import re
import sublime, sublime_plugin

class HtmlToStringCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        str_tag = '\''  # define the string tag
        join_tag = ','  # define the join tag
        sels = self.view.sel()
        print(len(sels))
        for sel in sels:
            ret = ''
            lines = self.view.lines(sel)
            for line in lines:
                frag = self.view.substr(line)
                match = re.match(r'^[\s|\t]*(\S).*(\S)\s*$', frag)
                if match == None: continue
                start = match.start(1)
                end = match.end(2) + 1
                ret = ret + frag[:start] + '\'' + frag[start:end]
                if lines.index(line) != len(lines) - 1:
                    ret = ret  + str_tag + join_tag + frag[end:] + '\n'
                else:
                    ret = ret + str_tag + frag[end:]
            self.view.replace(edit, sel, ret)