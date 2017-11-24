import wx
import wx.aui

class MyWindow(wx.Frame):

    def __init__(self, parent, title):
        super(MyWindow, self).__init__(parent, title = title, size = (300, 300))

        self.mgr = wx.aui.AuiManager(self)

        pnl = wx.Panel(self)
        pbox = wx.BoxSizer(wx.HORIZONTAL)
        text1 = wx.TextCtrl(pnl, -1, "Dockable", style = wx.NO_BORDER | wx.TE_MULTILINE)
        pbox.Add(text1, 1, flag = wx.EXPAND)
        pnl.SetSizer(pbox)

        info1 = wx.aui.AuiPaneInfo().Bottom()
        self.mgr.AddPane(pnl, info1)
        panel = wx.Panel(self)
        text2 = wx.TextCtrl(panel, size = (300, 200), style = wx.NO_BORDER|wx.TE_MULTILINE)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(text2, 1, flag = wx.EXPAND)

        panel.SetSizerAndFit(box)
        self.mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Center()
        self.Show(True)

    def OnClose(self, event):
        self.mgr.UnInit()
        self.Destroy()

app = wx.App()
MyWindow(None, "Dock Demo")
app.MainLoop()