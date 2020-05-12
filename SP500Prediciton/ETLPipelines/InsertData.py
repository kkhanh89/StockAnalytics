# Function to insert prices to database
def insert_price(conn, row, ticker):
	# Query
	query = """insert into stock.stockprice (ticker, tradedate, openprice, high, low,
            closeprice, volume) values (%s, %s, %s, %s, %s, %s, %s)"""
	# row must be a row from a pandas dataframe from yfinance
	data = (ticker, row['Date'], row['Open'], row['High'], row['Low'],
		    row['Close'], row['Volume'])
	cur = conn.cursor()
	cur.execute(query, data)
	

# Function to insert meta data to database
def insert_meta(conn, meta_dict):
	# Query
	query = """insert into stock.stockmeta (ticker, companyname,
	        gicssector, gicssubindustry, countrystockmarket, indexcomponent) 
	        values (%s, %s, %s, %s, %s, %s)"""
	# Take meta data store in dictionary
	data = (meta_dict['ticker'], meta_dict['companyname'],
		    meta_dict['gicssector'], meta_dict['gicssubindustry'], 
		    meta_dict['countrystockmarket'], meta_dict['indexcomponent'])
	cur = conn.cursor()
	cur.execute(query, data)
	conn.commit()
