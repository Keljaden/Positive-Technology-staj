from keycloak import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="https://idp.ptsecurity.com",
                                 client_id="pt",
                                 realm_name="internal",
                                 client_secret_key="19666a4f-32dd-4049-b082-684c74115f28")

# Get WellKnown
config_well_known = keycloak_openid.well_known()

# Get Token
token = keycloak_openid.token("givaschenkov", "w$b7*M9RzSHMxq")

# Get Userinfo
userinfo = keycloak_openid.userinfo(token['access_token'])
