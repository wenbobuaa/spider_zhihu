# -*- conding: utf-8 -*-
import mongoengine
from pymongo import MongoClient


client = MongoClient()
db = client.zhihu_data


class Zhihu_User_Profile():

    def __init__(
        self,
        user_name,
        user_be_agreed,
        user_be_thanked,
        user_followees,
        user_followers,
        user_education_school,
        user_education_subject,
        user_employment,
        user_employment_extra,
        user_location,
        user_gender,
        user_info,
        user_intro,
        user_url,
    ):
        self.user_name = user_name
        self.user_be_agreed = user_be_agreed
        self.user_be_thanked = user_be_thanked
        self.user_followees = user_followees
        self.user_followers = user_followers
        self.user_education_school = user_education_school
        self.user_education_subject = user_education_subject
        self.user_employment = user_employment
        self.user_employment_extra = user_employment_extra
        self.user_location = user_location
        self.user_gender = user_gender
        self.user_info = user_info
        self.user_intro = user_intro
        self.user_url = user_url

    def insert(self):
        db.user_profile.insert(
            {
                'user_name': self.user_name,
                'be_agreed': self.user_be_agreed,
                'be_thanked': self.user_be_thanked,
                'followees': self.user_followees,
                'followers': self.user_followers,
                'education_school': self.user_education_school,
                'education_subject': self.user_education_subject,
                'employment': self.user_employment,
                'employment_extra': self.user_employment_extra,
                'location': self.user_location,
                'gender': self.user_gender,
                'user_info': self.user_info,
                'user_intro': self.user_intro,
                'user_url': self.user_url
            }
        )

    def delete(self):
        db.user_profile.remove({"user_url": self.user_url})
