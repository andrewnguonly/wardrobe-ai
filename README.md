# Wardrobe AI

An AI agent for your wardrobe.

## Memory Structure

Namespace Hierarchy: 
- `<user_id>.articles.tops`
- `<user_id>.articles.bottoms`
- `<user_id>.articles.<custom>`
- `<user_id>.history`

Key: `<article_id>`

Value:
`<user_id>.articles.*`
```
{
    "description": ""
}
```

`<user_id>.history`
```
    "last_worn_at": "",
    "count": 0,
```
