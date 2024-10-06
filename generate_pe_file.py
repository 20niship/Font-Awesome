import json
import os

# 1. メタデータのJSONファイルをロード
metadata_file = './metadata/icons.json'

with open(metadata_file, 'r', encoding='utf-8') as f:
    icons_data = json.load(f)

# 2. フリーアイコンを保存しているフォルダ
svg_folder = './svgs/solid/'  # フリー版の場合 'solid' フォルダが使われる
svg_folder2 = './svgs/brands/'  # フリー版の場合 'solid' フォルダが使われる

# 3. SVGファイル名とUnicodeグリフを一致させる
icon_mapping = []

for icon_name, icon_info in icons_data.items():
    print(f'Processing {icon_name}., {icon_info["styles"]}')
    svg_filename = os.path.join(svg_folder, f'{icon_name}.svg')
    svg_filename2 = os.path.join(svg_folder2, f'{icon_name}.svg')
    unicode_value = icon_info.get('unicode', None)

    if os.path.exists(svg_filename):
        icon_mapping.append((svg_filename, unicode_value))
    elif os.path.exists(svg_filename2):
        icon_mapping.append((svg_filename2, unicode_value))

# 4. 一致したSVGファイル名とUnicode値を表示
for svg, unicode_value in icon_mapping:
    print(f'SVG: {svg}, Unicode: {unicode_value}')


def create_pe_file():
    str_ = f'''
# フォルダ内のSVGファイルを一括処理する例

# フォントを作成
New()
'''
    for svg, unicode_value in icon_mapping:
        str_ += f'Import("{svg}", "{unicode_value}")\n'

    str_ += '''
# TTFを生成
SetFontNames("CustomFont")
Generate("output_font.ttf")
Quit()
'''

    with open('custom-font-awesome.pe', 'w', encoding='utf-8') as f:
        f.write(str_)


create_pe_file()


