Imports System.IO
Imports System.Windows.Media.Animation
Imports Microsoft.Win32

Friend Module StartupHelper

    Public Function AddToStartup() As Boolean
        Dim key As RegistryKey = Registry.LocalMachine
        Dim key_path As String = "Software\Microsoft\Windows\CurrentVersion\Run"
        Dim value_name As String = "WallpaperGenerator"
        Dim script_path As String = Path.GetFullPath(Environment.GetCommandLineArgs()(0))
        Dim value_data As String = Environment.GetCommandLineArgs()(0) & " """ & script_path & """"

        Try
            Using reg_key As RegistryKey = key.OpenSubKey(key_path, True)
                reg_key.SetValue(value_name, value_data, RegistryValueKind.String)
            End Using

            Return True
        Catch ex As Exception
            Console.WriteLine(ex.Message)
            Return False
        End Try
    End Function

    Public Function IsAddedToStartup() As Boolean
        Dim key As RegistryKey = Registry.LocalMachine
        Dim key_path As String = "Software\Microsoft\Windows\CurrentVersion\Run"
        Dim value_name As String = "WallpaperGenerator"

        Try
            Using reg_key As RegistryKey = key.OpenSubKey(key_path, False)
                Dim value As Object = reg_key.GetValue(value_name)
                Dim script_path As String = Path.GetFullPath(Environment.GetCommandLineArgs()(0))
                Dim expected_value As String = Environment.GetCommandLineArgs()(0) & " """ & script_path & """"

                Return value IsNot Nothing AndAlso value.ToString() = expected_value
            End Using
        Catch ex As Exception
            Return False
        End Try
    End Function

    Public Function RemoveFromStartup() As Boolean
        Dim key As RegistryKey = Registry.LocalMachine
        Dim key_path As String = "Software\Microsoft\Windows\CurrentVersion\Run"
        Dim value_name As String = "WallpaperGenerator"

        Try
            Using reg_key As RegistryKey = key.OpenSubKey(key_path, True)
                reg_key.DeleteValue(value_name)
            End Using

            Return True
        Catch ex As Exception
            Return False
        End Try
    End Function

End Module

Public Class MainWindow
    Inherits Window

    Private script_path As String = Reflection.Assembly.GetEntryAssembly().Location
    Private script_directory As String = Path.GetDirectoryName(script_path)
    Private root_path As String = script_directory & Path.DirectorySeparatorChar

    Public Sub New()
        InitializeComponent()
        AddHandler Loaded, AddressOf MainWindow_Loaded
    End Sub

    Public Function IsProcessRunning(processName As String) As Boolean
        Dim processes As Process() = Process.GetProcessesByName(processName)
        Return processes.Length > 0
    End Function

    Private Sub save_Click(sender As Object, e As RoutedEventArgs) Handles save.Click
        If File.Exists(root_path & "limit.ini") = True AndAlso (PC.IsChecked = True OrElse Random.IsChecked = True OrElse Top.IsChecked = True) Then
            Dim unused3 = MessageBox.Show("您所选择的选项包含可能会生成包含 Restricted 18 类型的壁纸，由于限制配置，请您取消勾选【电脑壁纸】、【随机壁纸】或【AI 推荐】选项。若您已满18周岁，则请更换电脑后重试。", "R18 警告", MessageBoxButton.OK, MessageBoxImage.Warning)
        Else
            Dim configs As New List(Of String)()
            'Dim config As StreamWriter = File.CreateText(root_path & "RefreshSetting.Sr")
            Dim script_path1 As String = System.Reflection.Assembly.GetExecutingAssembly().Location
            Dim filename_with_extension As String = Path.GetFileName(script_path1)
            Dim filename_without_extension As String = Path.GetFileNameWithoutExtension(filename_with_extension)

            Dim ProgramPath As String = root_path & filename_without_extension & ".exe"

            If autostart.IsChecked = True Then

                Console.WriteLine(ProgramPath)

                Dim rst As Boolean = StartupHelper.AddToStartup()
                Console.WriteLine(rst)
                If rst = True Then
                    configs.Add("AutoStart")
                Else
                    If StartupHelper.IsAddedToStartup() = False Then
                        Dim unused2 = MessageBox.Show("启动项无法添加，因为权限不足，因此该条目失效。请尝试以管理员身份重新运行此程序以解决问题。", "意外的错误", MessageBoxButton.OK, MessageBoxImage.Error)
                    Else
                        Console.WriteLine("1. " & StartupHelper.IsAddedToStartup())
                        configs.Add("AutoStart")
                    End If
                End If
            Else
                If StartupHelper.IsAddedToStartup() = True Then
                    Dim rst As Boolean = StartupHelper.RemoveFromStartup()
                    If rst Then
                        ' Do nothing
                    Else
                        Dim unused1 = MessageBox.Show("启动项无法删除，因为权限不足，因此该条目失效。请尝试以管理员身份重新运行此程序以解决问题。", "意外的错误", MessageBoxButton.OK, MessageBoxImage.Error)
                        configs.Add("AutoStart")
                    End If
                End If
            End If

            If autochange.IsChecked = True Then
                configs.Add("AutoChange")
            End If

            If PC.IsChecked = True Then
                configs.Add("PC")
            ElseIf Starry.IsChecked = True Then
                configs.Add("Starry")
            ElseIf Top.IsChecked = True Then
                configs.Add("Top")
            Else
                configs.Add("Ran")
            End If

            Console.WriteLine(configs)

            ' 使用写入器将列表内容写入文件

            Using fs As New FileStream(root_path & "RefreshSetting.Sr", FileMode.Create, FileAccess.Write, FileShare.None)
                Using writer As New StreamWriter(fs)
                    For Each config_1 As String In configs
                        writer.WriteLine(config_1)
                    Next
                End Using
            End Using

            Console.WriteLine(ProgramPath)

            Dim unused = MessageBox.Show("配置已保存至本地，并将会立即生效", "已设置", MessageBoxButton.OK, MessageBoxImage.Information)

            End
        End If
    End Sub

    Private Sub nosave_Click(sender As Object, e As RoutedEventArgs) Handles nosave.Click
        End
    End Sub

    Private Sub about_Click(sender As Object, e As RoutedEventArgs) Handles about.Click
        Dim unused = MessageBox.Show("名称：壁纸生成器 3.0 图片生成插件 - 托盘自动壁纸程序" & Environment.NewLine &
                "依赖API：MirlKoiAPI" & Environment.NewLine &
                "        API源：https://api.iw233.cn/api.php" & Environment.NewLine &
                "        打包：思锐工作室" & Environment.NewLine, "关于", MessageBoxButton.OK, MessageBoxImage.Information)
    End Sub

    Private Sub MainWindow_Loaded(sender As Object, e As RoutedEventArgs) Handles Me.Loaded

        Dim isRunning As Boolean = IsProcessRunning("AutoWpChange_V2")  '调试的时候检测notepad，打包时记得修改
        If isRunning Then

            Dim startStoryboard As Storyboard = TryCast(FindResource("Start"), Storyboard)
            ' 当Storyboard资源存在时，播放动画
            startStoryboard.Begin()

            Dim filePath As String = root_path & "RefreshSetting.Sr"

            If File.Exists(filePath) = False Then
                autochange.IsChecked = True
                autostart.IsChecked = True
                PC.IsChecked = True
            Else
                Dim user_config As StreamReader = File.OpenText(root_path & "RefreshSetting.Sr")
                Dim user_setting = user_config.ReadToEnd()
                user_config.Close()

                ' 根据配置修改状态
                If user_setting.Contains("AutoStart") Then
                    autostart.IsChecked = True
                End If

                If user_setting.Contains("AutoChange") Then
                    autochange.IsChecked = True
                End If

                If user_setting.Contains("PC") Then
                    PC.IsChecked = True
                ElseIf user_setting.Contains("Starry") Then
                    Starry.IsChecked = True
                ElseIf user_setting.Contains("Top") Then
                    Top.IsChecked = True
                Else
                    Random.IsChecked = True
                End If
            End If

        Else
            Hide()
            Dim executablePath As String = Reflection.Assembly.GetEntryAssembly().Location
            Dim programDirectory As String = Path.GetDirectoryName(executablePath)
            Dim batFilePath As String = Path.Combine(programDirectory, "AutoWpChange_V2.exe")
            Process.Start(batFilePath)
            End
        End If
    End Sub
End Class
