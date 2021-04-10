import streamlit
import yfinance


streamlit.title(' Simple App To Read Stock Markets')

stock_name= streamlit.text_input('write the company name','GOOGL').upper()

streamlit.subheader('Stock Recommand')

stock_ticker = yfinance.Ticker(stock_name)

streamlit.dataframe(stock_ticker.recommendations)

streamlit.subheader('stock spilts')

streamlit.dataframe(stock_ticker.splits)

streamlit.subheader('Stock Price history  over time')

streamlit.write(stock_ticker.history(period='max'))

tt = stock_ticker.history(period='max')
streamlit.line_chart(tt.Open)



period_of_stock=streamlit.sidebar.text_input('the period id','1d')

start_of_stock=streamlit.sidebar.text_input('the opening','2010-5-31')

end_of_stock=streamlit.sidebar.text_input('the closing','2020-5-31')


time_frame = stock_ticker.history(period=period_of_stock , start=start_of_stock ,end=end_of_stock)

streamlit.subheader('the stock history in particular period by your chocie ')

streamlit.line_chart(time_frame.Open)
streamlit.line_chart(time_frame.Close)
streamlit.line_chart(time_frame.Volume)
