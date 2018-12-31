from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.brandTable.getBrandById import *
from makeoverapp.v1.categoriesTable.getCategoryById import *

from datetime import datetime, timedelta
from collections import defaultdict

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def getStats(phone_no):

    week_tod_dict={}

    start_dt = datetime.now() - timedelta(days=7)
    prev_day = datetime.now() - timedelta(days=1)
    end_date = datetime.now() + timedelta(days=1)

    week_tod_dict['pending_orders_today'] = order.objects.filter(timestamp__gt = prev_day, status='Pending').count()
    week_tod_dict['pending_orders_week'] = order.objects.filter(timestamp__gte = start_dt, timestamp__lt = end_date, status='Pending').count()

    week_tod_dict['cancelled_orders_today'] = order.objects.filter(timestamp__gt = prev_day, status='Cancelled').count()
    week_tod_dict['cancelled_orders_week'] = order.objects.filter(timestamp__gte = start_dt, timestamp__lt = end_date, status='Cancelled').count()

    week_tod_dict['received_orders_today'] = order.objects.filter(timestamp__gt = prev_day, status='Received').count()
    week_tod_dict['received_orders_week'] = order.objects.filter(timestamp__gte = start_dt, timestamp__lt = end_date, status='Received').count()

    week_tod_dict['on_hold_orders_today'] = order.objects.filter(timestamp__gt = prev_day, status='On Hold').count()
    week_tod_dict['on_hold_orders_week'] = order.objects.filter(timestamp__gte = start_dt, timestamp__lt = end_date, status='On Hold').count()

    week_tod_dict['processed_orders_today'] = order.objects.filter(timestamp__gt = prev_day, status='Processed').count()
    week_tod_dict['processed_orders_week'] = order.objects.filter(timestamp__gte = start_dt, timestamp__lt = end_date, status='Processed').count()

    count_dict={}
    for single_date in daterange(start_dt, end_date):
        order_count = order.objects.filter(timestamp__gt = single_date - timedelta(days=1), timestamp__lt = single_date + timedelta(days=1)).count()
        date_str=single_date.strftime('%d %b')
        count_dict[date_str] = order_count

    top_products={}
    cat_brand = product.objects.values('category_id', 'brand_id').distinct()

    for obj in cat_brand:
        product_table_ids = product.objects.filter(category_id = obj['category_id'], brand_id = obj['brand_id'])
        brand_name = getBrandById(obj['brand_id']).name
        category_name = getCategoryById(obj['category_id']).name
        key = brand_name + '_' + category_name
        shade_dict=defaultdict(lambda:0)
        for product_table_id in product_table_ids:
            shade_name=product.objects.get(id=product_table_id.id).product_id
            order_qty = sum(order_products.objects.filter(product_table_id=product_table_id.id).values_list('quantity', flat=True))
            shade_dict[shade_name] += order_qty

        top_products[key] = shade_dict

    ans_dict={'part_1': week_tod_dict, 'part_2': count_dict, 'part_3': top_products}

    return ans_dict
