from ystockquote import get_historical_prices
import datetime
import MySQLdb
import shlex

# connection = MySQLdb.connect (host = "localhost" , user = "root" ,passwd = "baapp@321" , db = "tests")
# cursor = connection.cursor()

def new_update_data():
#     select_ticker = "select distinct(ticker) from cmpdata_2015"
#     cursor.execute(select_ticker)
#     ticker_list = cursor.fetchall()
#     total_ticker = []
#     for each_ticker in ticker_list:
#         total_ticker.append(shlex.split("".join(each_ticker)))
    total_ticker = ['GOOG']
    start_date = '1950-01-01'
    next_date = '2015-05-20'
    
    for each_ticker in total_ticker:
#         try:
#             select_date_query = "select date from cmpdata_2015 where ticker = %s"
#             cursor.execute(select_date_query,each_ticker)
#             all_date = cursor.fetchall()
#         except Exception as e:
#             print e
#             print "error during date fatching",each_ticker
#             continue
#         last_updated_date = max(all_date)[0]
#         last_updated_date = last_updated_date + datetime.timedelta(days=1)
#         print "last updated date for the ticker",last_updated_date,each_ticker
#         last_updated_year = last_updated_date.year
#         last_updated_month = last_updated_date.month
#         if last_updated_month >= 1 and last_updated_month <=9:
#             last_updated_month = str(0) + str(last_updated_month)
#         last_updated_day = last_updated_date.day 
#         if last_updated_day >= 1 and last_updated_day <= 9:
#             last_updated_day = str(0) + str(last_updated_day)
#         next_date = str(last_updated_year) + '-' + str(last_updated_month) + '-' + str(last_updated_day)
        
        try:
            
            data = get_historical_prices(''.join(each_ticker),start_date,next_date)
        except:
            continue
        try:
            import ipdb;ipdb.set_trace()
            for each_key in sorted(data.keys(),key=str):
                nxt_dict = data[each_key]
                ticker = ''.join(each_ticker)
                updatin_date = each_key
                updatin_date = datetime.datetime.strptime(updatin_date,'%Y-%m-%d')
                open = nxt_dict['Open']
                high = nxt_dict['High']
                low = nxt_dict['Low']
                close = nxt_dict['Close']
                volume = nxt_dict['Volume']
                
#                 insert_data = "insert into cmpdata_2015(ticker,date,open,high,low,close,volume) VALUES(%s,%s,%s,%s,%s,%s,%s)"
#                 VALUES = (ticker,updatin_date,open,high,low,close,volume)
#                 cursor.execute(insert_data,VALUES)
#                 connection.commit()
                print "Successfully saved", each_ticker
        except:
            continue
new_update_data()
