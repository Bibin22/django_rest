from rest_framework.throttling import UserRateThrottle


class WatchListThrottlle(UserRateThrottle):
    scope = 'watchlist'


class WatchListDetails(UserRateThrottle):
    scope = 'watch_list_detail'