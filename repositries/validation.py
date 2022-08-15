from models.user import DSP
from models.ssp import Ad_Request
import requests, validators
MAX_KEYWORDS = 20


class Validator:
    def validate_dsp(dsp : DSP):
        msg = []
        if len(dsp.username) < 3:
            msg.append("username must be at least 3 characters")
        if len(dsp.password) < 8:
            msg.append("password must have at least 8 characters")
        if not Validator.validate_url(dsp.nego_api):
            msg.append("nego_api is not valid")
        if not Validator.validate_url(dsp.interactive_nego_api):
            msg.append("interactive_nego_api is not valid")
        if not Validator.validate_url(dsp.request_api):
            msg.append("request_api is not valid")
        if not Validator.validate_url(dsp.interactive_request_api):
            msg.append("interactive_request_api is not valid")
        if msg:
            return msg
        return False


    def validate_ad_request(ad_request :Ad_Request):
            msg = []
            if ad_request.min_cpc < 0:
                msg.append("min_cpc must be positive")
            if ad_request.categories:
                ad_request.categories = list(set(ad_request.categories))
            if ad_request.keywords:
                ad_request.keywords = list(set(ad_request.keywords))
                if len(ad_request.keywords) > MAX_KEYWORDS:
                    msg.append("too many keywords")
            if msg:
                return msg
            return False
    
    def validate_url(url):
        return validators.url(url)