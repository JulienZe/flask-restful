from flask_restful import Resource

from handlers.post_hander import PostHandler
from models.query_models.post_model import PostQueryModel
from models.response_models.post_model import ResponsePostModel
from resources import ApiResponse, schema


class Post(Resource):
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def get(self, topic_id, post_id):
        post = PostHandler(topic_id=topic_id, post_id=post_id).get_post()
        return ApiResponse().ok(post)

    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def put(self, topic_id, post_id):
        kwargs = self.parsed_args
        post = PostHandler(topic_id, post_id).update_post(**kwargs)

        return ApiResponse().ok(post)

    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def delete(self, topic_id, post_id):
        PostHandler(topic_id, post_id).delete_post()

        return ApiResponse().ok()


class Posts(Resource):
    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def get(self, topic_id):
        kwargs = self.parsed_args
        posts = PostHandler(topic_id).get_posts(**kwargs)

        return ApiResponse().ok(posts)

    @schema(query_model=PostQueryModel, response_model=ResponsePostModel)
    def post(self, topic_id):
        kwargs = self.parsed_args
        post = PostHandler(topic_id).create_post(**kwargs)
        return ApiResponse().ok(post)
