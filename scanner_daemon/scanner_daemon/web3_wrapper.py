from web3 import Web3
from web3.datastructures import AttributeDict
from web3.middleware import geth_poa_middleware
from hexbytes import HexBytes
import json
from metadata import Meta

RPC_URL_HTTP = Meta.RPC_URL_HTTP

# WALLET_ADDRESS = Meta.WALLET_ADDRESS
# TRANSACTION_ID = Meta.TRANSACTION_ID
# BLOCK_HASH = Meta.BLOCK_HASH

# web3 provider (infura.io)
web3 = Web3(Web3.HTTPProvider(RPC_URL_HTTP))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # middleware for PoA-based TestNet connection.


def _select_data_type(obj, data_type='hexbytes'):
    if data_type in ['hex', 'hexbytes']:
        return obj

    elif data_type in ['str', 'string']:
        return convert_dict_json_serializable(obj)


def _dict_without_keys(dictionary, keys):
    return {key: dictionary[key] for key in dictionary if key not in keys}


def _convert_data_json_serializable(data):  # recursive

    if data is None:
        return None
    elif isinstance(data, HexBytes):
        return data.hex()
    elif isinstance(data, list):
        return [_convert_data_json_serializable(ele) for ele in data]
    elif isinstance(data, dict) or isinstance(data, AttributeDict):
        data = dict(data)
        for key, val in data.items():
            data[key] = _convert_data_json_serializable(val)
        return data
    else:
        return data


def convert_dict_json_serializable(dictionary):
    for key, val in dictionary.items():
        dictionary[key] = _convert_data_json_serializable(val)
    return dictionary


def pretty_print_dict(obj):
    """
    특정 딕셔너리 내의 모든 HexBytes/Bytes 데이터를 recursive하게 string으로 변환
    """
    if type(obj) not in [dict, AttributeDict]:
        raise Exception

    dictionary = dict(obj)
    serializable = convert_dict_json_serializable(dictionary)

    pretty_json = json.dumps(serializable, indent=4)
    print(pretty_json)


def get_latest_block_number():
    return web3.eth.get_block_number()


def get_block_header(block_identifier, data_type='hexbytes'):
    block = dict(web3.eth.get_block(block_identifier))
    block_header = _dict_without_keys(block, ['transactions'])

    return _select_data_type(block_header, data_type)


def get_transactions_from_block(block_identifier, data_type='hexbytes'):
    block = dict(web3.eth.get_block(block_identifier))

    return _select_data_type(block, data_type)


def get_block(block_identifier, data_type='hexbytes'):  # block header + transactions
    block = dict(web3.eth.get_block(block_identifier))

    return _select_data_type(block, data_type)


def get_transaction(trx_hash, data_type='hexbytes'):
    transaction = dict(web3.eth.get_transaction(trx_hash))

    return _select_data_type(transaction, data_type)


def get_transaction_receipt(trx_hash, data_type='hexbytes'):
    receipt = dict(web3.eth.get_transaction_receipt(trx_hash))

    return _select_data_type(receipt, data_type)
