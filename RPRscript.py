class QueryProcessing:
    def __init__(self) -> None:
        self.verify = True
        self.headers = {"Accept": "application/json"}

    def get(self, url: str, params: dict = None) -> dict:
        from requests import get
        response = get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()["data"]
        else:
            return -response.status_code


class DataProcessing:
    def __init__(self, data: dict) -> None:
        self.data = data

    def search(self, section) -> list[...]:
        return [el[section] for el in self.data["content"]]

    def get_all(self) -> int:
        """all data pack"""
        return len(self.data["content"])

    def get_id_title(self) -> dict[int, str]:
        """id && title pack"""
        return {
            el["id"]: el["title"] for el in self.data["content"]
        }

    def get_tags(self) -> dict[int, str]:
        """id && tag pack"""
        return {
            el["id"]: el["title"] for el in self.data["content"]
        }

    def get_id_auth(self) -> dict[int, str]:
        """id pack && author pack"""
        return {
            el["id"]: el["author"]["name"] for el in self.data["content"]
        }


class PCP:
    """Processing Content Pack"""
    # @TODO: реализовать обработку запросаов для контент-паков
    def __init__(self, data: dict) -> None:
        self.data = data
