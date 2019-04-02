# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    # 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    # 'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'x-ab-param': 'tp_discussion_feed_type_android=2;top_billab=0;top_recall=7;top_recall_tb_short=61;top_thank=1;top_new_user_rec=0;top_recall_tb_long=51;top_billvideo=0;top_core_session=-1;tp_sft=a;se_majorob_style=0;top_recall_deep_user=1;top_video_score=1;tp_favsku=a;se_boost=1;top_nad=1;top_ydyq=X;ls_new_score=1;top_billpic=0;top_nucc=0;top_rank=9;se_auto_syn=0;se_time_search=new;top_rerank_reformat=2;se_click2=0;tp_discussion_feed_card_type=2;top_login_card=1;top_tr=0;top_feedre_itemcf=33;top_root_ac=1;top_sj=2;ls_new_video=1;top_recall_exp_v1=1;se_ad_index=2;se_entity=on;top_raf=n;top_ebook=0;top_recall_core_interest=81;top_brand_content=2;top_f_r_nb=1;gw_guide=0;se_websearch=0;se_correct_ab=0;pin_efs=orig;top_feedre=1;se_mfq=0;top_new_user_gift=0;top_30=0;top_vd_gender=0;top_billupdate1=3;se_daxuechuisou=new;qa_answerlist_ad=0;se_new_market_search=on;soc_brandquestion=1;top_distinction=0;top_no_weighing=1;se_search_feed=Y;tp_qa_metacard=1;top_card=-1;top_test_4_liguangyi=1;se_minor_onebox=d;top_ntr=1;tp_write_pin_guide=3;se_consulting_switch=off;se_engine=1;top_ab_validate=3;top_root_web=0;se_major_onebox=major;top_cc_at=1;zr_art_rec=base;se_consulting_price=n;top_root_few_topic=0;se_gemini_service=content;se_wiki_box=1;top_newfollowans=0;tp_header_style=0;tp_sticky_android=0;top_followtop=1;top_recall_tb=5;top_yc=0;top_universalebook=1;pf_creator_card=1;pin_ef=orig;se_filter=1;top_newfollow=0;top_new_feed=1;top_bill=0;top_feedre_rtt=41;top_wonderful=1;tp_dis_version=0;se_ltr_v1=0;se_spb309=0;top_recall_follow_user=91;top_root_mg=1;zr_ans_rec=gbrank;top_feedre_cpt=101;top_is_gr=0;top_newuser_feed=1;top_recall_tb_follow=71;top_root=1;top_scaled_score=0;top_limit_num=0;se_billboardsearch=0;se_colos=0;tp_qa_metacard_top=0;top_fqai=2;ls_is_use_zrec=0;top_quality=0;top_v_album=1;top_yhgc=0;ls_topic_is_use_zrec=1;top_follow_reason=0;top_gif=0;se_prf=0;top_user_gift=0;se_backsearch=1;top_mt=0;top_topic_feedre=21',
    # 'x-requested-with': ' fetch',
    # 'x-udid': 'AMBlJQQhbQ6PTi8PVBytA61iQI8hUb4mD18=',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuSpiderMiddleware': 543,
# }

# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuSpiderMiddleware': 543,
#    'zhihuuser.middlewares.RandomUserAgentMiddleware': 542,
#    'zhihuuser.middlewares.ProxyMiddleware': 541,
#    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
# }

# DOWNLOADER_MIDDLEWARES = {
#     'zhihuuser.middlewares.ProxyMiddleware': 125,
# }
#
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# SPLASH_URL = 'http://192.168.99.100:8050'
MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'  # mongo里面仓库的名字

# SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# SCHEDULER_FLUSH_ON_START = True
PROXY_URL = 'http://127.0.0.1:5000/get'
