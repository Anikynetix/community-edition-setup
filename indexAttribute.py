#functions to be added in setup.py

def create_local_db_index(self, attributeName, indexType):
	self.run([self.dspath, 'dsconfig create-local-db-index',
		'--backend-name', 'userRoot',
		'--type', 'generic',
		'--index-name', attributeName,
		'--set index-type:', indexType,
		'--set index-entry-limit:', '4000',
		'--hostName', 'localhost',
		'--port', '4444',
		'--bindDN', self.ldap_binddn,
		'-j', self.ldapPassFn,
		'--trustAll',
		'--noPropertiesFile',
		'--no-prompt'])

def set_backend_prop(self, attributeName, setEnabledStatus):
	self.run([self.dspath, 'dsconfig set-backend-prop',
		'--backend-name', 'userRoot',
		'--set enabled:', setEnabledStatus,
		'--hostName', 'localhost',
		'--port', '4444',
		'--bindDN', self.ldap_binddn,
		'-j', self.ldapPassFn,
		'--trustAll',
		'--noPropertiesFile',
		'--no-prompt'])

def rebuild_index(self, attributeName):
	self.run([self.dspath, 'rebuild-index',
		'--bindDN', 'o=gluu',
		'--set index', attributeName])