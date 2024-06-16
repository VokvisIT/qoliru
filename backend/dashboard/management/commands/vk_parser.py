from django.core.management.base import BaseCommand
from dashboard.models import Region, Source, Resource, ModelDataTest
from .parser_vk import get_vk_wall_posts, get_group_id
from datetime import datetime, timedelta
import pytz
from tqdm import tqdm
from django.utils import timezone

def get_last_post_date(resource):
    try:
        last_post = ModelDataTest.objects.filter(resource=resource, source__name='Telegram').latest('data', 'time')
        last_post_date = timezone.make_aware(timezone.datetime.combine(last_post.data, last_post.time), timezone.get_current_timezone())
        return last_post_date
    except ModelDataTest.DoesNotExist:
        print(f"No posts found for resource {resource.name}.")
        return None
class Command(BaseCommand):
    help = 'Parse VK data for the last day'

    def handle(self, *args, **options):
        token = 'vk1.a.5uEA0WWcvx91FS4UhMFvjdRzjJCoV1JlijQphi0paAaocmJysNkFvhxGL40l7SSrUDHSBHo7waTME8bC38pYqrjURbgsW0Dn8MfVOJ98d753CZOfLgN_MpDFDEZ7GcLp1u_Ga9dQA2pv83N6h4pQY6q97Nt6JPx88ZmtzHTszQe_bNeX4Ecj4yYgTcYtd2GTKe9QPLj0bANiyWZFhsNI3w'
        version = '5.131'
        end_date = datetime.now(pytz.timezone('Europe/Moscow')) - timedelta(days=1)
        resources = Resource.objects.filter(source__name='ВКонтакте')
        for resource in resources:
            group_id = get_group_id(token, version, resource.link)
            if group_id is not None:
                last_post = ModelDataTest.objects.filter(resource=resource, source__name='ВКонтакте').latest('data', 'time')
                moscow_tz = pytz.timezone('Europe/Moscow')
                last_post_date = moscow_tz.localize(datetime.combine(last_post.data, last_post.time))
                get_vk_wall_posts(token, version, group_id, last_post_date, resource.name, resource)
