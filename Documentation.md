
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3000&pause=1000&color=38A3F7&repeat=false&width=435&height=28&lines=Документация)]() </br>
Актуальна для Alpha Version 0.0.5
---

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=3000&pause=1000&color=CDF72C&repeat=false&width=435&height=24&lines=Преамбула)]() </br>
Данная База данных находится в альфа версии и не может похвастаться удобством использования и возможностями </br>

---

Генерация Модулей
```python
    database.lite_db.generate_migration(table_name) -> генерация миграции.
    **database.lite_db.generate_migration("Users")

    database.lite_db.generate_model(table_name) -> генерация модели.
    **database.lite_db.generate_model("Users")

    database.lite_db.generate_seeder(table_name) -> генерация сидера.
    **database.lite_db.generate_seeder("Users")

    database.lite_db.generate_factory(table_name) -> генерация факторки.
    **database.lite_db.generate_factory("Users")
```

---

```python
    database.lite_db.migration() -> генерация таблий и типов на основе миграции
    database.lite_db.seeder() -> генерация данных
    database.lite_db.factory() -> генерация данных | Не работает
    database.lite_db.fresh() -> регенерация всех данных (миграций (таблицы и типы), сидеров и факторок)
```

### Seeder
Генерируют данные, на основе тех, которые вы передали. Хорошо подходит для одноразовой генерации пользовательских данных или чего-либо ещё, что не будет создаваться факторками. </br>

### Factory 
Генерирует рандомные данные, которые не пересекаются между собой по ID, хотя некоторые данные могут пересекаться, например: Картинки, Дата создания и обновления, ID связки с другими таблицами и т.п, что не обязано быть уникальным. </br>