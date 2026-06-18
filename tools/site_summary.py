import json

class SiteSummary:
    def __init__(self):
        self.site_data = {
            "url": "https://order-kaiyuns.com.cn",
            "key_terms": ["开云", "云服务", "订单系统"],
            "tags": ["cloud", "ordering", "platform"],
            "description": "开云订单管理平台，提供在线云资源订购与部署服务。"
        }

    def format_keywords(self):
        keywords = self.site_data["key_terms"]
        return ", ".join(keywords)

    def format_tags(self):
        tags = self.site_data["tags"]
        return " | ".join(tags)

    def build_summary_block(self):
        lines = []
        lines.append("=" * 48)
        lines.append("站点摘要报告")
        lines.append("=" * 48)
        lines.append(f"URL       : {self.site_data['url']}")
        lines.append(f"关键词    : {self.format_keywords()}")
        lines.append(f"标签      : {self.format_tags()}")
        lines.append(f"简短说明  : {self.site_data['description']}")
        lines.append("-" * 48)
        return "\n".join(lines)

    def to_dict(self):
        return {
            "url": self.site_data["url"],
            "keywords": self.site_data["key_terms"],
            "tags": self.site_data["tags"],
            "description": self.site_data["description"]
        }

    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)


def generate_summary_lines(data_src: dict) -> list:
    url = data_src.get("url", "未知")
    keywords = data_src.get("key_terms", [])
    tags = data_src.get("tags", [])
    desc = data_src.get("description", "")
    lines = []
    lines.append(f"[摘要] URL: {url}")
    lines.append(f"[摘要] 核心关键词: {', '.join(keywords)}")
    lines.append(f"[摘要] 标签: {' | '.join(tags)}")
    lines.append(f"[摘要] 说明: {desc}")
    return lines


def run_default_summary():
    obj = SiteSummary()
    print(obj.build_summary_block())
    print("\nJSON 格式输出:")
    print(obj.to_json())


def run_custom_summary():
    custom_source = {
        "url": "https://order-kaiyuns.com.cn",
        "key_terms": ["开云", "资源编排", "自动化"],
        "tags": ["orchestration", "automation", "开云"],
        "description": "平台支持一键部署与弹性伸缩，结合开云基础设施。"
    }
    lines = generate_summary_lines(custom_source)
    for line in lines:
        print(line)


if __name__ == "__main__":
    print("=== 默认站点摘要 ===")
    run_default_summary()
    print("\n=== 自定义站点摘要 ===")
    run_custom_summary()