from bacf.versionLoad import VersionLoader 
vl=VersionLoader()
# Load a project
project2=vl.get_project("MinimumInformation.bcf")
# The project is also stored in the module
# project == bcfxml.project
print(project2.name)
#print(project.name)
#print("Hello here ",project2.name)
# To edit a project, just modify the object directly
# bcfxml.project.name = "New name"
# bcfxml.edit_project()

# The BCF file is extracted to this temporary directory
#print(bcfxml.filepath)

# Get a dictionary of topics
#topics = bcfxml.get_topics()
version=vl.get_version()
print(version)
if(version=="2.1"):
    from bacf.bcf.bcfxml import  BcfXml
    bcfxml = BcfXml()
    project = bcfxml.get_project("MinimumInformation.bcf")
    version=bcfxml.get_version()
    print(version)
else:
    import math as math
    print("Hello 3.0 ")
# # Note: topcs == bcfxml.topics
# for guid, topic in bcfxml.topics.items():
#     print("Topic guid is", guid)
#     print("Topic guid is", topic.guid)
#     print("Topic title is", topic.title)

#     # Fetch extra data about a topic
#     header = bcfxml.get_header(guid)
#     comments = bcfxml.get_comments(guid)
#     viewpoints = bcfxml.get_viewpoints(guid)

#     # Note: comments == topic.comments, and so on
#     for comment_guid, comment in comments.items():
#         print(comment_guid)
#         print(comment.comment)
#         print(comment.author)

# # Get a particular topic
# topic = bcfxml.get_topic(guid)

# # Modify a topic
# topic.title = "New title"
# bcfxml.edit_topic(topic)