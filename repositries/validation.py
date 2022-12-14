from models.user import DSP, DSPUpdate
from models.ssp import Ad_Request
import  validators
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
        if not Validator.validate_url(dsp.html_request_api):
            msg.append("html_request_api is not valid")
        if not Validator.validate_url(dsp.html_interactive_request_api):
            msg.append("html_interactive_request_api is not valid")
        if msg:
            return msg
        return False

    def validate_dsp_update(dsp_update : DSPUpdate):
        msg = []
        if dsp_update.password:
            if len(dsp_update.password) < 8:
                msg.append("password must have at least 8 characters")
        if dsp_update.nego_api:
            if not Validator.validate_url(dsp_update.nego_api):
                msg.append("nego_api is not valid")
        if dsp_update.interactive_nego_api:
            if not Validator.validate_url(dsp_update.interactive_nego_api):
                msg.append("interactive_nego_api is not valid")
        if dsp_update.request_api:
            if not Validator.validate_url(dsp_update.request_api):
                msg.append("request_api is not valid")
        if dsp_update.interactive_request_api:
            if not Validator.validate_url(dsp_update.interactive_request_api):
                msg.append("interactive_request_api is not valid")
        if dsp_update.html_request_api:
            if not Validator.validate_url(dsp_update.html_request_api):
                msg.append("html_request_api is not valid")
        if dsp_update.html_interactive_request_api:
            if not Validator.validate_url(dsp_update.html_interactive_request_api):
                msg.append("html_interactive_request_api is not valid")
        if msg:
            return msg
        return False

    def validate_user_update(user_update : DSPUpdate):
        msg = []
        if len(user_update.password) < 8:
            msg.append("password must have at least 8 characters")
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
            if len(ad_request.payment_account) == 0:
                msg.append("payment_account must not be empty")
                
            if ad_request.max_width != 0:
                if ad_request.max_width < 5:
                    msg.append("width must be greater than 5px")

            if ad_request.max_height != 0:
                if ad_request.max_height < 5:
                    msg.append("height must be greater than 5px")
            
            if msg:
                return msg
            return False
    
    def validate_url(url):
        return validators.url(url)