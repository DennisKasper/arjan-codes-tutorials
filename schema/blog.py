from ariadne import ObjectType
from graphql import GraphQLResolveInfo
from data import Author, Blog, BlogPayload, all_blogs, get_blog, update_blog, get_author

from schema.types import query, mutation

BLOG_TYPEDEF = '''
    type Blog {
        id: ID!
        title: String!
        content: String!
        author: Author!
    }

    input BlogPayload {
        title: String
        content: String
    }

    type Mutation {
        update_blog(blog_id: ID!, blog_payload: BlogPayload!): Blog
    }
'''


blog_query = ObjectType('Blog')


@query.field('blogs')
def resolve_blogs(_, info: GraphQLResolveInfo) -> list[Blog]:
    return all_blogs()


@query.field('blog')
def resolve_blog(_, info: GraphQLResolveInfo, blog_id: int) -> Blog:
    return get_blog(blog_id)


@mutation.field('update_blog')
def resolve_update_blog(_, info: GraphQLResolveInfo, blog_id: int, blog_payload: BlogPayload) -> Blog:
    return update_blog(blog_id, blog_payload)


@blog_query.field('author')
def resolve_author(blog, info: GraphQLResolveInfo) -> Author:
    return get_author(blog['author_id'])

