from instagrapi.types import UserShort
from pydantic_core import Url


def get_following():
    # Use fake followers and following dicts
    _following = {'369174195': UserShort(pk='369174195', username='creativityasia', full_name='CreativityAsia',
                                         profile_pic_url=Url(
                                             'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/105987205_257981148819170_4506076318207388579_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=102&_nc_ohc=f5dKSfITsQIAb7EJVY1&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfDaycnx1MEA2vSt7z8G7PCu8L-HQfeMcQsy89Hm1416Wg&oe=66301582&_nc_sid=ce9561'),
                                         profile_pic_url_hd=None, is_private=False),
                  '649553524': UserShort(pk='649553524', username='juncturemedia', full_name='Juncture Media',
                                         profile_pic_url=Url(
                                             'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/14073170_848979778570780_1376379920_a.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=104&_nc_ohc=dNqi_uBYNPkAb6bTzKb&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfBKX2sdQ1B1ojuBGc-c3WvehlIQGTm4cp1YY8x6sVCjqw&oe=66300750&_nc_sid=ce9561'),
                                         profile_pic_url_hd=None, is_private=False),
                  '3043973126': UserShort(pk='3043973126', username='raisethebarapp', full_name='afewguys apps 📱',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/1389776_243020599375486_1216656588_a.jpg?_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=110&_nc_ohc=sNT4v43V8qoAb6EmJCR&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfDOAAOFmiNRi5QH0BkEAf2HMJj6fJFBp6uu6HkAxnnVBg&oe=6630082E&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '3519564570': UserShort(pk='3519564570', username='meagerquest_series', full_name='Meager Quest',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/13561739_1699625306968272_1251239353_a.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=100&_nc_ohc=fqofh6aWpJAAb5pkx5m&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfDwZlewKBY5tZaDCr4XwLPoYay9jLik27BMDd53OrLbuQ&oe=6630296C&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '3967731338': UserShort(pk='3967731338', username='meming.life', full_name='Funny Instagram Memes',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/37525441_209082383108100_2822068898185084928_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=100&_nc_ohc=NaHtBNP-5RIAb5unjp9&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfC_w3-aYQWjpZeR4cVHC8IxTTcA2GxtVEjaf2taTUBInA&oe=6630005D&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '4032894284': UserShort(pk='4032894284', username='leindastudios', full_name='Leinda Studios',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/19428940_276925066107044_5986639684216815616_a.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=108&_nc_ohc=AZlOykHkusIAb5e6epl&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfDobYmpxdI5sNMHKj1o3yO9ln7O_Zb4xHLSy4crbeNDUg&oe=6630222D&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '4039193757': UserShort(pk='4039193757', username='gaming.lulz8', full_name='gaming.lulz8',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/37315879_260714024657623_8973041534454726656_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=107&_nc_ohc=cTz8lpEAJBkAb5X4P8O&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfBlLUfItxWrKcgpPuZXueTYYjBcvnWfwohjUWJcIGJxLQ&oe=662FFFA7&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '4061391973': UserShort(pk='4061391973', username='gaming.humor1', full_name='Gaming.humor1',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/14723592_1284080961656745_5370456166667124736_a.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=109&_nc_ohc=mPioEcGQzmYAb5H0kez&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfD1spqhZIOk8P8yd78fElnqwnInMyn-X9oNZImS0HWkoQ&oe=6630086E&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '4186980843': UserShort(pk='4186980843', username='appsirgames', full_name='AppSir Games',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/128156135_741714713220051_424241413684764878_n.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=103&_nc_ohc=iufulBx6SFcAb5Sut1l&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfDIP5z3WpCeTcmdevhvc_ibGI_6ORZshPZaLqhbjstQzg&oe=66300F19&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  '4217922187': UserShort(pk='4217922187', username='playmotivegames', full_name='Playmotive',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/14719281_1805448229708902_1284307663747809280_a.jpg?stp=dst-jpg_e0_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=106&_nc_ohc=0tO-wtg7244Ab4gozCR&edm=ALB854YBAAAA&ccb=7-5&oh=00_AfAZRw_GrtTQXITM5bCP-vJIlI6k_CIyN49-g3O4-lvKEQ&oe=66301FE4&_nc_sid=ce9561'),
                                          profile_pic_url_hd=None, is_private=False),
                  }
    return _following


def get_followers():
    _followers = {'7187074786': UserShort(pk='7187074786', username='indikator_space', full_name='Indikator',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/62655654_197385984515165_6211206576183705600_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=105&_nc_ohc=uduLa-WN8p8Ab77ro6z&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfDUZUK8dQ1n8u08tzei2cZpaSocoU3GPoxsiPrbYxJwpA&oe=66300E06&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '6952444048': UserShort(pk='6952444048', username='__igdo__', full_name='IGDO', profile_pic_url=Url(
                      'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/26185261_432555357164041_5879827554122072064_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=101&_nc_ohc=yYI37_MiHD0Ab5Fa5m8&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfBY2K4X-Ocfy7kHqD_EmDKEmqA3Yhp3X8x3kK8Gk1iHEQ&oe=662FF84E&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '5645314263': UserShort(pk='5645314263', username='sambelandme', full_name='StClair Cordice',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/19424719_486180515052886_1166483533858865152_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=110&_nc_ohc=l1_0LKxJDvoAb73SNLy&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfB6yzQCvsi5r_GOf6LFhJOygBjMLD-W6sLFi3VyKaTWWQ&oe=662FF879&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '4648223761': UserShort(pk='4648223761', username='vivanox', full_name='Vivanox', profile_pic_url=Url(
                      'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/16906158_746491202195215_7373371666455330816_a.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=107&_nc_ohc=SXUG8GRnSx0Ab5U9Ywn&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfCa9LKugq9rwDbEBeV4In9WJTI0kTUa_dp6EZpEYuFQpw&oe=66300A2F&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '6230160842': UserShort(pk='6230160842', username='phantom_king0v0', full_name='Duron James',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/152204074_129410565735817_2307004558166796015_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=101&_nc_ohc=TC-vQugog-UAb5Hd5g_&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfCFjjOkYLJlQ_osXrqPGlyj6UEO6Lxb-I8VSoMX7AhFKg&oe=663018D9&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '2916339956': UserShort(pk='2916339956', username='yieldgame', full_name='', profile_pic_url=Url(
                      'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/12716693_1677060159215756_762003967_a.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=108&_nc_ohc=AzuBYmufIFsAb5F2ZSI&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfAHmos_x5Tx7pW0jsGR_Nc6nwELBOR5VyhMzRFaQGdnqw&oe=662FFE12&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '6069354596': UserShort(pk='6069354596', username='star_drifters', full_name='Star Drifters',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/21879693_281144699056825_1840279360465010688_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=101&_nc_ohc=qiBIBnKVcgkAb6u11Gw&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfDNSgnxPK0ge_wo_8AP9_-3p_V7V9sNgcL-PB1IlLcJbA&oe=66301217&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '3043973126': UserShort(pk='3043973126', username='raisethebarapp', full_name='afewguys apps 📱',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/1389776_243020599375486_1216656588_a.jpg?_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=110&_nc_ohc=sNT4v43V8qoAb6EmJCR&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfBvoQIwCipnIzLktRhNAKci6P4MZr6TNtKCyXjIIItxOw&oe=6630082E&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '3519564570': UserShort(pk='3519564570', username='meagerquest_series', full_name='Meager Quest',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/13561739_1699625306968272_1251239353_a.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=100&_nc_ohc=fqofh6aWpJAAb5pkx5m&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfDYiCi0UJQco9rHiCDMneA4BY8jvENMqVdVLEhOhEwmUA&oe=6630296C&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  '369174195': UserShort(pk='369174195', username='creativityasia', full_name='CreativityAsia',
                                         profile_pic_url=Url(
                                             'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/105987205_257981148819170_4506076318207388579_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=102&_nc_ohc=f5dKSfITsQIAb7EJVY1&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfAo6e4xJnodW2v3pA4Po7XLO0eO7siEqS6xZAau_t152g&oe=66301582&_nc_sid=17ea04'),
                                         profile_pic_url_hd=None, is_private=None),
                  '4217922187': UserShort(pk='4217922187', username='playmotivegames', full_name='Playmotive',
                                          profile_pic_url=Url(
                                              'https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/14719281_1805448229708902_1284307663747809280_a.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=106&_nc_ohc=0tO-wtg7244Q7kNvgEgozCR&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AfDgCuKlPLpsSYF9H5BAEl0ubvDO57YaEUKlIiIPA-HDPQ&oe=66301FE4&_nc_sid=17ea04'),
                                          profile_pic_url_hd=None, is_private=None),
                  }
    return _followers
