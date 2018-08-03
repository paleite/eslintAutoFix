import sublime, sublime_plugin
import platform

SETTINGS_KEY = 'StylelintAutoFix.sublime-settings'
DEFAULT_STYLELINT_PATH = ''
DEFAULT_SHOW_PANEL = True

IS_WINDOWS = platform.system() == 'Windows'

class Preferences:
  def load(self, settings):
    self.stylelint_path = settings.get('stylelint_path', DEFAULT_STYLELINT_PATH)
    self.show_panel = settings.get('show_panel', DEFAULT_SHOW_PANEL)

Pref = Preferences()

def plugin_loaded():
  settings = sublime.load_settings(SETTINGS_KEY)
  Pref.load(settings)
  settings.add_on_change('reload', lambda: Pref.load(settings))

class Stylelint_auto_fixCommand(sublime_plugin.WindowCommand):
	def run(self):
		fileName = self.window.active_view().file_name();
		args = {
		  'cmd': [
		    'stylelint',
		    '--fix',
		    '--no-ignore',
		    fileName
		  ],
		  'path': Pref.stylelint_path,
		  'shell': IS_WINDOWS
		}
		self.window.run_command('exec', args)
		if not Pref.show_panel:
		  self.window.run_command("hide_panel", {"panel": "output.exec"})



