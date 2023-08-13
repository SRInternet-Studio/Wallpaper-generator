Imports System.ComponentModel
Imports System.Drawing
Imports System.Drawing.Text

Public Class Window5
    Private colordialog1 As System.Windows.Forms.ColorDialog
    Private colordialog2 As System.Windows.Forms.ColorDialog
    Public R1
    Public G1
    Public B1
    Public R2
    Public G2
    Public B2
    Private Sub button1_MouseLeftButtonUp(sender As Object, e As MouseButtonEventArgs) Handles button1.MouseLeftButtonUp

    End Sub

    Private Sub button1_Click(sender As Object, e As RoutedEventArgs) Handles button1.Click
        colordialog1 = New Forms.ColorDialog
        colordialog1.ShowDialog()
        R1 = colordialog1.Color.R
        G1 = colordialog1.Color.G
        B1 = colordialog1.Color.B
        textblock4.Background = New SolidColorBrush(System.Windows.Media.Color.FromRgb(R1, G1, B1))
        textblock4.Text = R1 & ", " & G1 & ", " & B1
        button1.IsEnabled = False
        button2.IsEnabled = True
    End Sub
    Private Sub button2_Click(sender As Object, e As RoutedEventArgs) Handles button2.Click
        colordialog2 = New Forms.ColorDialog
        colordialog2.ShowDialog()
        R2 = colordialog2.Color.R
        G2 = colordialog2.Color.G
        B2 = colordialog2.Color.B
        textblock2.Background = New SolidColorBrush(System.Windows.Media.Color.FromRgb(R2, G2, B2))
        textblock2.Text = R2 & ", " & G2 & ", " & B2
        button2.IsEnabled = False
        button4.IsEnabled = True
        button4_Copy.IsEnabled = True
    End Sub
    Private Sub button3_Click(sender As Object, e As RoutedEventArgs) Handles button3.Click
        button1.IsEnabled = True
        button2.IsEnabled = False
        button4.IsEnabled = False
        button4_Copy.IsEnabled = False
        textblock4.Background = System.Windows.Media.Brushes.White()
        textblock4.Text = "没有颜色"
        textblock2.Background = System.Windows.Media.Brushes.White()
        textblock2.Text = "没有颜色"
    End Sub
    Private Sub button4_Click(sender As Object, e As RoutedEventArgs) Handles button4.Click
        'Dim myLinearGradientBrush = New LinearGradientBrush With {
        '    .StartPoint = New Point(combobox2.Text.ToString(), combobox1.Text.ToString()), '颜色在窗口底部的左右位置、0是最左，颜色在窗口右侧的上下位置、1是最右
        '    .EndPoint = New Point(combobox4.Text.ToString(), combobox3.Text.ToString()) '颜色在窗口底部的左右位置、0是最左，颜色在窗口右侧的上下位置、1是最右
        '    }
        Dim startPoint As New Windows.Point(Double.Parse(combobox2.Text), Double.Parse(combobox1.Text))
        Dim endPoint As New Windows.Point(Double.Parse(combobox4.Text), Double.Parse(combobox3.Text))

        Dim myLinearGradientBrush As New LinearGradientBrush With {
            .StartPoint = startPoint,
            .EndPoint = endPoint
        }
        myLinearGradientBrush.GradientStops.Add(New GradientStop(System.Windows.Media.Color.FromRgb(R1, G1, B1), 0.0))
        myLinearGradientBrush.GradientStops.Add(New GradientStop(System.Windows.Media.Color.FromRgb(R2, G2, B2), 1.0))
        Dim window1 = Application.Current.MainWindow
        window1.Background = myLinearGradientBrush
        window1.Show()
    End Sub

    Private Sub button4_Copy_Click(sender As Object, e As RoutedEventArgs) Handles button4_Copy.Click
        Dim myLinearGradientBrush = New LinearGradientBrush With {
    .StartPoint = New Windows.Point(combobox2.Text.ToString(), combobox1.Text.ToString()), '颜色在窗口底部的左右位置、0是最左，颜色在窗口右侧的上下位置、1是最右
    .EndPoint = New Windows.Point(combobox4.Text.ToString(), combobox3.Text.ToString()) '颜色在窗口底部的左右位置、0是最左，颜色在窗口右侧的上下位置、1是最右
    }
        myLinearGradientBrush.GradientStops.Add(New GradientStop(System.Windows.Media.Color.FromRgb(R1, G1, B1), 0.0))
        myLinearGradientBrush.GradientStops.Add(New GradientStop(System.Windows.Media.Color.FromRgb(R2, G2, B2), 1.0))
        Background = myLinearGradientBrush
    End Sub

    Private Sub Window5_Closing(sender As Object, e As CancelEventArgs) Handles Me.Closing
        End
    End Sub

    Private Sub button4_Copy2_Click(sender As Object, e As RoutedEventArgs) Handles button4_Copy2.Click
        Dim window1 As New Window1
        window1.ShowDialog()
    End Sub

    Private Sub button5_Click(sender As Object, e As RoutedEventArgs) Handles button5.Click
        Process.Start("壁纸生成器V3.exe")
    End Sub

    Private Sub button5_Copy_Click(sender As Object, e As RoutedEventArgs) Handles button5_Copy.Click
        Process.Start("https://afdian.net/a/srinternet")

    End Sub
    Private Sub InstallFont(fontPath As String)
        ' 创建一个字体集合对象
        Using fontCollection As New PrivateFontCollection()
            ' 向字体集合中添加字体文件
            fontCollection.AddFontFile(fontPath)

            ' 安装字体到系统中
            Dim fontsCount As Integer = fontCollection.Families.Length
            fontCollection.Families(fontsCount - 1).ToString()
        End Using
    End Sub

    Private Sub button5_Copy1_Click(sender As Object, e As RoutedEventArgs) Handles button5_Copy1.Click
        Dim fontExists As Boolean = FontChecker.CheckFont("DingTalk JinBuTi")
        If fontExists Then
            Console.WriteLine("字体存在")
        Else
            Console.WriteLine("字体不在")
            InstallFont("DingTalk_JinBuTi_Regular.ttf")
        End If
        Process.Start("自动更换壁纸.exe")
    End Sub

    Private Sub Presets_Click(sender As Object, e As RoutedEventArgs) Handles Presets.Click
        SetGradientBackground()
    End Sub

    Private Sub SetGradientBackground()
        ' 创建一个颜色数组，指定多个渐变色
        Dim colors As System.Windows.Media.Color() = {System.Windows.Media.Colors.Red, System.Windows.Media.Colors.Yellow, System.Windows.Media.Colors.Green, System.Windows.Media.Colors.Blue}

        ' 创建一个GradientStopCollection，指定每个渐变色的位置和比例
        Dim gradientStops As New GradientStopCollection()
        For i As Integer = 0 To colors.Length - 1
            gradientStops.Add(New GradientStop(colors(i), i / (colors.Length - 1)))
        Next

        ' 创建一个LinearGradientBrush对象，设置渐变起始点和结束点，并使用GradientStopCollection
        Dim gradientBrush As New LinearGradientBrush(gradientStops, New System.Windows.Point(0, 0), New System.Windows.Point(0, 1))

        ' 将渐变画刷应用于窗口背景
        Background = gradientBrush
    End Sub
End Class
Public Class FontChecker
    Public Shared Function CheckFont(fontName As String) As Boolean
        ' 获取系统中安装的字体集合
        Dim fontFamilies As New System.Collections.ObjectModel.ReadOnlyCollection(Of System.Windows.Media.FontFamily)(Fonts.SystemFontFamilies)

        ' 遍历字体集合，检查是否存在目标字体
        For Each fontFamily As System.Windows.Media.FontFamily In fontFamilies
            If String.Equals(fontFamily.Source, fontName, StringComparison.OrdinalIgnoreCase) Then
                Return True ' 目标字体存在
            End If
        Next

        Return False ' 目标字体不存在
    End Function
End Class
