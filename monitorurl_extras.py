
'''
    def test_method_metrics_status( self ):
        print("------------------------ Test Case 3 ---------------------")
        x = testObject.status_code
        print(x)
        print("------------------ Test Case 3 Completion-----------------")

    def test_method_api_response ( self ) :
        response = my_file.app.test_client().get('/metrics')
        self.assertEqual ( response.status_code , 200 )
        print("API Response Code:", response.status_code )
        print ( "---Test 4" )

    def test_method_collector_200 ( self ) :
        x , y = my_file.CustomCollector.url_resp(self, URL="https://httpstat.us/200")
        print("x=== {}, y===== {}".format(x,y))
        print ( "---Test 5" )

    def test_method_collector_503 ( self ) :
        print(my_file.REGISTRY.register(my_file.CustomCollector()))
        print ( "---Test 6" )
'''


print(f"Response Status==== {http_status}")
    print(f"Response Latency===== {response_latency}")
    print("------------------ Test Case 1 Completion-----------------")

    def successTest(self):
          print("------------------------ Test Case 2 ---------------------")
          http_status, response_latency = monitorURL.readConfig("https://httpstat.us/200")
          print(f"Response Status==== {http_status}")
          print(f"Response Latency===== {response_latency}")
          print("------------------ Test Case 2 Completion-----------------")

          def test_latency(self):
                warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
                response1, response2 = monitorURL.checkURL("https://httpstat.us/503")
                #rint(response1, response2)
                randomDecimal = decimal.Decimal(random.randrange(0.0, 2.0))/100
                self.assertAlmostEqual(response2, float(randomDecimal))

                class Test_MainProgram(unittest.TestCase):
                    def test_method_api_response ( self ) :
                        response = my_file.main.test_client().get('/metrics')
                        self.assertEqual ( response.status_code , 200 )
                        print("API Response Code:", response.status_code )
                        print ( "---Test 4" )

                    def test(self):
                        pass

                        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
                            print(f"Collector Class Instantiation : {source_code.REGISTRY.register(source_code.CustomCollector())}")


                            readinessProbe:
                              httpGet:
                                path: /
                                port: 8000
                              initialDelaySeconds: 10
