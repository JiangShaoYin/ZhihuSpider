# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class CommentItem(Item):
    id = Field()
    author = Field()
    allow_delete = Field()
    allow_like = Field()
    allow_reply = Field()
    allow_vote = Field()
    can_collapse = Field()
    can_recommend = Field()
    censor_status = Field()
    child_comment_count = Field()
    child_comments = Field()
    collapsed = Field()
    content = Field()
    created_time = Field()
    disliked = Field()
    featured = Field()
    is_author = Field()
    is_delete = Field()
    resource_type = Field()
    reviewing = Field()
    type = Field()
    url = Field()
    vote_count = Field()
    voting = Field()
    avatar_pic1 = Field()
    avatar_pic2 = Field()
    avatar_pic3 = Field()

class UserItem(Item):
    # define the fields for your item here like:
    # id = Field()
    # name = Field()
    # avatar_url = Field()
    # headline = Field()
    # description = Field()
    # url = Field()
    url_token = Field()
    # gender = Field()
    # cover_url = Field()
    # type = Field()
    # badge = Field()
    #
    # answer_count = Field()
    # articles_count = Field()
    # commercial_question_count = Field()
    # favorite_count = Field()
    # favorited_count = Field()
    # follower_count = Field()
    # following_columns_count = Field()
    # following_count = Field()
    # pins_count = Field()
    # question_count = Field()
    # thank_from_count = Field()
    # thank_to_count = Field()
    # thanked_count = Field()
    # vote_from_count = Field()
    # vote_to_count = Field()
    # voteup_count = Field()
    # following_favlists_count = Field()
    # following_question_count = Field()
    # following_topic_count = Field()
    # marked_answers_count = Field()
    # mutual_followees_count = Field()
    # hosted_live_count = Field()
    # participated_live_count = Field()
    #
    # locations = Field()
    # educations = Field()
    # employments = Field()

