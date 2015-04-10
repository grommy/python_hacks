from urllib import urlretrieve

class ImResizer(object):
	"""docstring for ClassName"""
	def __init__(self, link):
		self.link = link
				
	def link_fix(self,link):
		fixed_link=link.replace('http://','')	
		return fixed_link

	def post_constructor(self,width,height):
		post_link="https://images.weserv.nl/"+"?url="+self.link_fix(self.link)+"&h="+str(height)+"&w="+str(width)+"&t=absolute"
		return post_link

	def make_resized(self,width,height,folder):
		filename =dest_folder + link.strip().split('/')[-1].split('.')[-2] +'_'+str(width)+'x'+str(height)
		# print filename
		post_link=self.post_constructor(width,height)
		urlretrieve(post_link, filename)
		return True


link="http://savepic.su/5521161.png"
width=800
height=600
dest_folder="/home/nkondratiev/Downloads/"

Im2Resize=ImResizer(link)
Im2Resize.make_resized(width,height,dest_folder)