Imports System.ComponentModel
Imports System.IO

Public Class MainWindow
    Private ReadOnly savedialog As System.Windows.Forms.SaveFileDialog
    Private Sub MainWindow_Loaded(sender As Object, e As RoutedEventArgs) Handles Me.Loaded
        Application.Current.MainWindow = Me
        Dim make_window As New Window5
        make_window.Show()
        Hide()
    End Sub

    Private Sub save_Click(sender As Object, e As RoutedEventArgs) Handles save.Click
        Dim savedialog As New Forms.SaveFileDialog With {
            .Filter = "高质量位图文件 (*.bmp*)|*.bmp"
        }
        savedialog.ShowDialog()
        Dim filepath = savedialog.FileName
        If filepath = "" Then

        Else
            WindowState = WindowState.Maximized
            save.Visibility = Visibility.Hidden
            SaveWindowContent(Me, filepath)
            save.Visibility = Visibility.Visible
            Process.Start(filepath)
        End If
    End Sub

    Private Sub MainWindow_Closing(sender As Object, e As CancelEventArgs) Handles Me.Closing
        e.Cancel = True
        Hide()
    End Sub

    Private Sub MainWindow_Closed(sender As Object, e As EventArgs) Handles Me.Closed

    End Sub

    Public Function SaveWindowContent(source As Window, fileName As String)
        Dim elem As FrameworkElement
        elem = source.Content
        Dim targetBitmap As RenderTargetBitmap
        targetBitmap = New RenderTargetBitmap(elem.ActualWidth, elem.ActualHeight, 96D, 96D, PixelFormats.Default)
        targetBitmap.Render(source)
        Dim encoder As BmpBitmapEncoder
        encoder = New BmpBitmapEncoder()
        encoder.Frames.Add(BitmapFrame.Create(targetBitmap))
        Using fs As FileStream = File.Open(fileName, FileMode.OpenOrCreate)
            encoder.Save(fs)
        End Using
    End Function
End Class