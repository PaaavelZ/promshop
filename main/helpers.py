from  dataclasses import dataclass
from typing import Any

from dbcore.models import MainOffer, Offer, FullInfo, MainInfo, Info, SliderMainInfo, SliderInfo, SliderChildInfo


@dataclass
class GetContext:
    lang: str = ''

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.lang not in ('ru', 'kz', 'eng'):
            self.lang = 'kz'

        return {    
            'main_offer':self._get_main_offer(),
            'offers': self._get_offers(),
            'info_title': self._get_info_title(),
            'infos_no_slider': self._get_infos_with_no_slider(),
            'infos_slider': self._get_infos_with_slider(),
        }

    def _get_main_offer(self):
        return MainOffer.objects.filter(lang__name=self.lang).last()
    
    def _get_offers(self):
        return Offer.objects.filter(main_offer__lang__name=self.lang)
    
    def _get_info_title(self):
        return FullInfo.objects.filter(lang__name=self.lang).last()
    
    def _get_infos_with_no_slider(self):
        return MainInfo.objects.filter(full_info__lang__name=self.lang).prefetch_related('infos')
    
    def _get_infos_with_slider(self):
        return SliderMainInfo.objects.filter(lang__name=self.lang).prefetch_related('sliderinfos').prefetch_related('sliderinfos__sliderchildinfos')
    
    

