import sublime
import sublime_plugin

urlopen = None

try:
    import urllib.request
    urlopen = urllib.request.urlopen
except (ImportError) as e:
    import urllib2
    urlopen = urllib2.urlopen

class DownloadSourceCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel('Url:', '', self.on_done, None, None)

    def on_done(self, text):
        content = urlopen(text).read().decode('utf-8')
        view = self.window.new_file()

        view.run_command('insert_source', {'text': content})

class DownloadInsertSourceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel('Url:', '', self.on_done, None, None)

    def on_done(self, text):
        content = urlopen(text).read().decode('utf-8')
        self.view.run_command('insert_source', {'text': content})

class InsertSourceCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.replace(edit, self.view.sel()[0], text)
        current_sel = self.view.sel()[0]
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(current_sel.begin(), current_sel.begin()))
