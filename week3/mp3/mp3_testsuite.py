import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    # Create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # # Test reset function
    # suite.run_test(game_class.mc_trial,
    #     ,
    #     "Game was won:")