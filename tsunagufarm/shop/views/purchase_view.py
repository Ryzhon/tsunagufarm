from django.shortcuts import render, get_object_or_404
from ..models import Product
from django.http import JsonResponse
from django.shortcuts import render
import numpy as np

def purchase(request):
    product = get_object_or_404(Product, pk=1)
    context = {
        'header_text'   : 'Dynamic Header Text from View',
        'page_title'    : '購入画面',
        'product_name'  : product.name,
        'product_image' : product.img,
        'product_shop'  : product.shop,
    }
    
    return render(request, 'purchase.html', context)

def purchase_after(request):
    product = get_object_or_404(Product, pk=1)
    request.user.bought_shops.add(product.shop)
    context = {
        'header_text'   : 'Dynamic Header Text from View',
        'page_title'    : '購入画面',
        'product_name'  : product.name,
        'product_image' : product.img,
        'product_shop'  : product.shop,
    }
    return render(request, 'purchase_after.html', context)

# def qr_decode_opencv(img):
#     img_array = np.array(img)
#     img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

#     detector = cv2.QRCodeDetector()

#     # QRコードを検出
#     retval, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(img_bgr)

#     if retval:  # True if at least one QR code has been found
#         # 1つ以上のQRコードが検出された場合、最初のものだけを返す
#         return decoded_info[0]
#     else:
#         return None

# def upload_qrcode(request):
#     if request.method == 'GET':
#         return render(request, "upload_qrcode.html")

#     elif request.method == 'POST':
#         uploaded_file = request.FILES.get("qrcode_image")


#         if uploaded_file:
#             image = Image.open(uploaded_file)
#             decoded_data = qr_decode_opencv(image)
#             print(decoded_data)
#             print(image)
#             print("----------------------")

#             if decoded_data:
#                 return JsonResponse({"qr_content": decoded_data})
#             else:
#                 return JsonResponse({"error": "No QR codes found."}, status=400)

#         return JsonResponse({"error": "No file uploaded."}, status=400)