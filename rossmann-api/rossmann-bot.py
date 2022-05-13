import pandas as pd
import json
import requests
import os

from flask import Flask, request, Response

#constants
TOKEN = '5353329871:AAEiBr1u-eWkE540Vr6d66t3bzQ-fVYeWMw'

#info about bot
#https://api.telegram.org/bot5353329871:AAEiBr1u-eWkE540Vr6d66t3bzQ-fVYeWMw/getMe

# get updates
#https://api.telegram.org/bot5353329871:AAEiBr1u-eWkE540Vr6d66t3bzQ-fVYeWMw/getUpdates

# WEBHook
#https://api.telegram.org/bot5353329871:AAEiBr1u-eWkE540Vr6d66t3bzQ-fVYeWMw/setWebhook?url=https://34a3-2804-14c-65c1-4b37-4c94-429b-3084-a907.sa.ngrok.io

#heroku
#https://api.telegram.org/bot5353329871:AAEiBr1u-eWkE540Vr6d66t3bzQ-fVYeWMw/setWebhook?url=https://dashboard.heroku.com/apps/rossmann--bot
# send message
#https://api.telegram.org/bot5353329871:AAEiBr1u-eWkE540Vr6d66t3bzQ-fVYeWMw/sendMessage?chat_id=5361113923&text=Hi Vadia, I am doing good, tanks

def send_message( chat_id, text ):
	url = 'https://api.telegram.org/bot{}/'.format( TOKEN )
	url = url + 'sendMessage?chat_id={}'.format( chat_id ) 
	
	r = requests.post( url, json={'text': text} )
	print( 'Status Code {}'.format( r.status_code ) )
	
	return None

def load_dataset( store_id ):
	# loading test dataset
	df10 = pd.read_csv( 'test.csv' )
	df11 = pd.read_csv( 'store.csv', low_memory=False )

	# merge test dataset + stored
	df_test = pd.merge( df10, df11, how='left', on='Store')

	# chose store for rpediction
	df_test = df_test[df_test['Store'] == store_id ]
	
	if not df_test.empty:

		# remoive closed days
		df_test = df_test[df_test['Open'] != 0 ]
		df_test = df_test[~df_test['Open'].isnull()]
		df_test = df_test.drop( 'Id', axis=1 )
		
		#Convert DataFrame to json
		data = json.dumps( df_test.to_dict( orient='records' ) )
	else:
		data = 'error'
	
	return data

def predict( data ):
	# API call
	url= ' https://rossmann--sales--prediction.herokuapp.com/rossmann/predict'
	header = {'Content-type': 'application/json'}
	data = data

	r = requests.post( url, data=data, headers=header )
	print( 'Status Code{}'.format( r.status_code ) )

	d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )
	
	return d1


def parse_message( message ):
	chat_id = message['message']['chat']['id']
	store_id = message['message']['text']
	
	store_id = store_id.replace( '/', '' )
	
	try:
		store_id = int( store_id )
	except ValueError:
		store_id = 'error'
		
	return chat_id, store_id
	
	

# API INITIALIZE
app = Flask( __name__ )

@app.route( '/', methods=['GET', 'POST'] )
def index():
	if request.method == 'POST':
		message = request.get_json()
		
		chat_id, store_id = parse_message( message )
		
		if  store_id != 'error':
			# loading data
			data = load_dataset( store_id )
			
			if data != 'error':
				# prediction
				d1 = predict( data )
				
				# calculation
				d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()
				
				#send message
				msg = 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format(
					d2['store'].values[0],
					d2['prediction'].values[0] )
				
				send_message( chat_id, msg )
				return Response( 'OK', status=200 )
				    
			
			else: 
				send_message( chat_id, "This store's ID prediction is not available, please insert an available ID" )
				return Response( 'OK', status=200 )
		else:
			send_message( chat_id, "The store's ID is wrong, please insert an available ID " )
			
			return Response( 'OK', status=200 )
	
	else:
		return '<h1> Rossmann Telegram BOT </h1>'

if __name__ == '__main__':
	port = os.environ.get( 'PORT', 5000 )
	app.run( host='0.0.0.0', port=port )
debug=True




