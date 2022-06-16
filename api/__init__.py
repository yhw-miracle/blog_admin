from flask_restful import Api
from api.article import ArticlesResource, ArticleResource
from api.category import CategoryResource
from api.tag import TagResource
from api.comment import CommentResource
from api.reading_notes import ReadingNotesResource

api = Api()
api.add_resource(ArticlesResource, "/")
api.add_resource(ArticleResource, "/article/")
api.add_resource(CategoryResource, "/category/")
api.add_resource(TagResource, "/tag/")
api.add_resource(CommentResource, "/comment/")
api.add_resource(ReadingNotesResource, "/reading_notes/")

