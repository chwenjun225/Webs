# Working:
- https://learning.oreilly.com/library/view/django-5-by/9781805125457/Text/Chapter_02.xhtml#_idParaDest-109
- https://learning.oreilly.com/library/view/django-5-by/9781805125457/Text/Chapter_04.xhtml#_idParaDest-150

# Running commands:
## MySite
python manage.py runserver
docker run --name=blog_db -e POSRGRES_DB=blog -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=P00778076 -p 5432:5432 -d postgres:16.2

# Bug logs:
1. ✔ Error when translate to Spain language (https://learning.oreilly.com/library/view/django-5-by/9781805125457/Text/Chapter_11.xhtml#_idParaDest-327)

2. ✔ 
```
ConnectionError at /en/6/living-room-sofas-and-chairs/
Error 111 connecting to localhost:6379. Connection refused.
Request Method:	GET
Request URL:	http://127.0.0.1:8000/en/6/living-room-sofas-and-chairs/
Django Version:	4.2.16
Exception Type:	ConnectionError
Exception Value:	
Error 111 connecting to localhost:6379. Connection refused.
Exception Location:	/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9/site-packages/redis/connection.py, line 282, in connect
Raised during:	shop.views.product_detail
Python Executable:	/home/chwenjun225/miniconda3/envs/Webs/bin/python
Python Version:	3.9.20
Python Path:	
['/home/chwenjun225/Webs/SynerSocial',
 '/home/chwenjun225/Webs/SynerSocial',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python39.zip',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9/lib-dynload',
 '/home/chwenjun225/miniconda3/envs/Webs/lib/python3.9/site-packages']
Server time:	Sun, 01 Dec 2024 16:35:56 +0000
```

# Dự án Foxer (AI-Agent)
### **Phân tích các bước công việc yêu cầu**
1. **Lập kế hoạch và ưu tiên các tác vụ:**
   - **Giai đoạn 1:** Nhắc nhở qua WeChat và email, tự động tải xuống và chấm điểm báo cáo.
   - **Giai đoạn 2:** Tự động tạo PPT báo cáo, gửi báo cáo cho giám đốc.
   - **Giai đoạn 3:** Quản lý điểm số và điểm danh qua Webex.

2. **Các công nghệ cần áp dụng:**
   - **Quản lý thông báo và nhắc nhở:** Sử dụng API của WeChat, email server.
   - **Xử lý báo cáo:** Tích hợp xử lý ngôn ngữ tự nhiên (NLP) để chấm điểm báo cáo.
   - **Tự động tạo PPT:** Dùng Python với thư viện như `python-pptx`.
   - **Quản lý cuộc họp:** API của Webex để thu thập danh sách tham dự và bảng điểm.

3. **Mô hình AI Agent:**
   - **Logic điều khiển:** Kết hợp giữa tác nhân dựa trên quy tắc và AI học máy (Machine Learning).
   - **Chấm điểm thông minh:** Finetune LLaMA để phân tích ngữ cảnh và đánh giá nội dung báo cáo.

### **Kế hoạch phát triển**
- **Giai đoạn 1:** 
  - Phát triển module nhắc nhở và thu thập báo cáo.
  - Tích hợp công cụ xử lý ngôn ngữ tự nhiên để chấm điểm tự động.
- **Giai đoạn 2:**
  - Tạo và tự động hóa quy trình làm PPT báo cáo.
  - Gửi báo cáo cho giám đốc và xử lý phản hồi.
- **Giai đoạn 3:**
  - Triển khai module quản lý điểm số và điểm danh.
  - Đánh giá hiệu quả và điều chỉnh.

### **Lợi ích dài hạn**
- Giảm tải công việc hành chính, giúp nhân viên tập trung vào nhiệm vụ quan trọng hơn.
- Tăng cường độ chính xác và nhất quán trong việc quản lý báo cáo và cuộc họp.
- Tối ưu hóa chi phí vận hành, mang lại giá trị kinh tế rõ rệt.

Bạn có muốn tập trung vào bước nào trước hay cần hỗ trợ thêm phần chi tiết nào không? 😊