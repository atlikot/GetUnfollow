from views.Router import Router, DataStrategyEnum
from views.Login import Login
from views.Profile import Profile
from views.Settings import Settings
from views.Dashboard import Dashboard

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": Login,
  "/profile": Profile,
  "/settings": Settings,
  "/data": Dashboard,
}