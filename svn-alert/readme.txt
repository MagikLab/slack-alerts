slack_channel_tokens.py  chứa danh sách cấu hình xác định cập nhật của repo nào sẽ được post vào kênh nào
slack_svn.py : code chính
hooks : chứa 2 file cấu hình hook vào svnserver. 1 file dành cho linux, 1 file dành cho windows.
	+ Chỉnh 2 file này lại để trỏ tới đúng tới thư mục chứa file skack_svn.py
	+ Sau đó copy file nào thư mục hooks của các repo muốn cảnh báo.
	
slack_channel_tokens_Magik.zip chua thong tin cau hinh cua Magik.
password : ho va ten day du cua cau thu dau tien cua MagikLab bi "treo gio".