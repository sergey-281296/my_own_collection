#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2025 Sergey
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Создаёт текстовый файл на удалённом хосте
version_added: "1.0.0"
description:
    - Модуль создаёт файл по указанному пути с заданным содержимым.
options:
    path:
        description:
            - Абсолютный путь к создаваемому файлу.
        required: true
        type: str
    content:
        description:
            - Содержимое файла.
        required: true
        type: str
author:
    - Sergey (@sergey-281296)
'''

EXAMPLES = r'''
- name: Создать файл /tmp/test.txt с содержимым "Hello"
  my_own_module:
    path: /tmp/test.txt
    content: "Hello"
'''

RETURN = r'''
path:
    description: Путь к созданному файлу
    returned: success
    type: str
    sample: /tmp/test.txt
content:
    description: Содержимое файла
    returned: success
    type: str
    sample: Hello
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path
    result['content'] = content

    if module.check_mode:
        # В режиме check просто сообщаем, что изменение будет
        if not os.path.exists(path) or open(path).read() != content:
            result['changed'] = True
        module.exit_json(**result)

    # Реальная запись файла
    try:
        current_content = ''
        if os.path.exists(path):
            with open(path, 'r') as f:
                current_content = f.read()
        if current_content != content:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        module.exit_json(**result)
    except Exception as e:
        module.fail_json(msg=str(e), **result)

def main():
    run_module()

if __name__ == '__main__':
    main()
