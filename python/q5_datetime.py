# Hint:  use Google to find python function

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

import pandas as pd
return pd.to_datetime(date_start) - pd.to_datetime(date_stop)


####b)
date_start = '12312013'
date_stop = '05282015'

x = datetime.strptime('12312013', '%m%d%Y')
y = datetime.strptime('05282015', '%m%d%Y')

return (y - x).days

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
import pandas as pd
return pd.to_datetime(date_start) - pd.to_datetime(date_stop)
