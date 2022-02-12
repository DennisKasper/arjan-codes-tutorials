from schema.types import query
from graphql import GraphQLResolveInfo
from data import Author,  all_authors, get_author

AUTHOR_TYPEDEF = '''
    type Author {
        id: ID!
        name: String!
    }
'''


@query.field('authors')
def resolve_authors(_, info: GraphQLResolveInfo) -> list[Author]:
    return all_authors()


@query.field('authors')
def resolve_author(_, info: GraphQLResolveInfo, author_id: int) -> Author:
    return get_author(author_id)
