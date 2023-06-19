operators = {
    "lt": "<",
    "gt": ">",
    "eq": "==",
    "ne": "!=",
    "le": "<=",
    "ge": ">=",
}

update_operations = {
    "add": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
    "shl": "<<",
    "shr": ">>",
}

assembly_operations = ["stop",
                       "add",
                       "sub",
                       "mul",
                       "div",
                       "sdiv",
                       "mod",
                       "smod",
                       "exp",
                       "not",
                       "lt",
                       "gt",
                       "slt",
                       "sgt",
                       "eq",
                       "iszero",
                       "and",
                       "or",
                       "xor",
                       "byte",
                       "shl",
                       "shr",
                       "sar",
                       "addmod",
                       "mulmod",
                       "signextend",
                       "keccak256",
                       "pop",
                       "mload",
                       "mstore",
                       "mstore8",
                       "sload",
                       "sstore",
                       "msize",
                       "gas",
                       "address",
                       "balance",
                       "selfbalance",
                       "caller",
                       "callvalue",
                       "calldataload",
                       "calldatasize",
                       "calldatacopy",
                       "codesize",
                       "codecopy",
                       "extcodesize",
                       "extcodecopy",
                       "returndatasize",
                       "returndatacopy",
                       "extcodehash",
                       "create",
                       "create2",
                       "call",
                       "callcode",
                       "delegatecall",
                       "staticcall",
                       "return",  # end execution, return data mem[p…(p+s)) 'return(p, s)'
                       'revert',
                       "selfdestruct",
                       "invalid",
                       "log0",
                       "log1",
                       "log2",
                       "log3",
                       "log4",
                       "chainid",
                       "basefee",
                       "origin",
                       "gasprice",
                       "blockhash",
                       "coinbase",
                       "timestamp",
                       "number",
                       "difficulty",
                       "prevrandao",
                       "gaslimit"]