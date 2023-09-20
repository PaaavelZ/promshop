from  dataclasses import dataclass
from typing import Any

from dbcore.models import MainPage, Offer, ChildOffer, Info, CategoryInfo


@dataclass
class GetContext:
    lang: str = ''

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.lang not in ('ru', 'kz', 'eng'):
            self.lang = 'kz'

        return {    
            'lang': self.lang,
            'main_page': self._get_main_page(),
            'main_offer': self._get_main_offer(),
            'offers': self._get_offers(),
            'info_title': self._get_info_title(),
            'infos_no_slider': self._get_infos_with_no_slider(),
        }

    def _get_main_page(self):
        return MainPage.objects.filter(lang__name=self.lang).last()

    def _get_main_offer(self):
        return Offer.objects.filter(lang__name=self.lang).last()
    
    def _get_offers(self):
        return ChildOffer.objects.filter(offer__lang__name=self.lang)
    
    def _get_info_title(self):
        return Info.objects.filter(lang__name=self.lang).last()
    
    def _get_infos_with_no_slider(self):
        return CategoryInfo.objects.filter(info__lang__name=self.lang).prefetch_related('childcategoryinfos')
    
    

