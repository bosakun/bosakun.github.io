---
layout: home
---

某通信制大学の情報系1年。AIとセキュリティの境目あたりに興味があります。  
基本的にXにいるので、覗きに来てください。  
時々更新します。  

- LLMエージェントのセキュリティ
- フィジカルAI/VLAへの敵対的攻撃
- 機械学習・LLMコンペ
- LLMの構築（gpt-ossレベル）

{%- comment -%}
  ここから下を index.md の好きな位置に貼り付けてください。
  site.data.zenn は _data/zenn.json を Jekyll が自動で読み込んだものです。
{%- endcomment -%}

## 書いたもの

{% if site.data.zenn and site.data.zenn.size > 0 %}
<ul class="zenn-list">
{%- for post in site.data.zenn %}
  <li>
    <a href="{{ post.link }}">{{ post.title }}</a>
    {%- if post.date %} <time datetime="{{ post.date }}">{{ post.date }}</time>{% endif %}
  </li>
{%- endfor %}
</ul>

<p><a href="https://zenn.dev/naoyabone">Zenn で全部見る →</a></p>
{% else %}
<p><a href="https://zenn.dev/naoyabone">Zenn に記事を書いています →</a></p>
{% endif %}

<style>
.zenn-list { list-style: none; padding: 0; }
.zenn-list li { padding: .6rem 0; border-bottom: 1px solid #e5e5e5; }
.zenn-list a { text-decoration: none; }
.zenn-list time { display: block; font-size: .8rem; color: #888; margin-top: .2rem; }
</style>

## Links

- [X (@BoSaBoSa_ja)](https://x.com/BoSaBoSa_ja)
- [GitHub](https://github.com/bosakun)

## Mail
naomobmail@gmail.com
