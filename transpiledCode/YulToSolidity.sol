pragma solidity >=0.4.22 <0.9.0;


contract Token
{
    assembly {
        sstore(0,caller())
        caller()
    }
    //datacopy(0,dataoffset("runtime"),datasize("runtime")) function datacopy not declared
    //dataoffset("runtime") function dataoffset not declared
    //datasize("runtime") function datasize not declared
    assembly {
        return(0,datasize("runtime"))
        //datasize("runtime") function datasize not declared
    }
}
contract runtime
{
    require(iszero(callvalue()));
    iszero(callvalue());
    callvalue();
    if (selector() == 0x70a08231)
    {
        returnUint(balanceOf(decodeAsAddress(0)));
        balanceOf(decodeAsAddress(0));
        decodeAsAddress(0);
    }
    else if (selector() == 0x18160ddd)
    {
        returnUint(totalSupply());
        totalSupply();
    }
    else if (selector() == 0xa9059cbb)
    {
        transfer(decodeAsAddress(0),decodeAsUint(1));
        decodeAsAddress(0);
        decodeAsUint(1);
        returnTrue();
    }
    else if (selector() == 0x23b872dd)
    {
        transferFrom(decodeAsAddress(0),decodeAsAddress(1),decodeAsUint(2));
        decodeAsAddress(0);
        decodeAsAddress(1);
        decodeAsUint(2);
        returnTrue();
    }
    else if (selector() == 0x095ea7b3)
    {
        approve(decodeAsAddress(0),decodeAsUint(1));
        decodeAsAddress(0);
        decodeAsUint(1);
        returnTrue();
    }
    else if (selector() == 0xdd62ed3e)
    {
        returnUint(allowance(decodeAsAddress(0),decodeAsAddress(1)));
        allowance(decodeAsAddress(0),decodeAsAddress(1));
        decodeAsAddress(0);
        decodeAsAddress(1);
    }
    else if (selector() == 0x40c10f19)
    {
        mint(decodeAsAddress(0),decodeAsUint(1));
        decodeAsAddress(0);
        decodeAsUint(1);
        returnTrue();
    }
    else
    {
        assembly {
            revert(0,0)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function mint(string account, string amount) public
    {
        require(calledByOwner());
        calledByOwner();
        mintTokens(amount);
        emitTransfer(0,account,amount);
    }
    // function params type can not be correctly inferred, please check manually
    function transfer(string to, string amount) public
    {
        executeTransfer(caller(),to,amount);
        caller();
    }
    // function params type can not be correctly inferred, please check manually
    function approve(string spender, string amount) public
    {
        revertIfZeroAddress(spender);
        setAllowance(caller(),spender,amount);
        caller();
        emitApproval(caller(),spender,amount);
        caller();
    }
    // function params type can not be correctly inferred, please check manually
    function transferFrom(string from, string to, string amount) public
    {
        decreaseAllowanceBy(from,caller(),amount);
        caller();
        executeTransfer(from,to,amount);
    }
    // function params type can not be correctly inferred, please check manually
    function executeTransfer(string from, string to, string amount) public
    {
        revertIfZeroAddress(to);
        deductFromBalance(from,amount);
        emitTransfer(from,to,amount);
    }
    // function params type can not be correctly inferred, please check manually
    function selector() public returns (string s)
    {
        assembly {
            div(calldataload(0),0x100000000000000000000000000000000000000000000000000000000)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function decodeAsAddress(string offset) public returns (string v)
    {
        v = decodeAsUint(offset);
        if (iszero(iszero(and(v,not(0xffffffffffffffffffffffffffffffffffffffff)))))
        {
            assembly {
                revert(0,0)
            }
        }
    }
    // function params type can not be correctly inferred, please check manually
    function decodeAsUint(string offset) public returns (string v)
    {
        assembly {
            add(4,mul(offset,0x20))
        }
        if (lt(calldatasize(),add(pos,0x20)))
        {
            assembly {
                revert(0,0)
            }
        }
        assembly {
            calldataload(pos)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function returnUint(string v) public
    {
        assembly {
            mstore(0,v)
        }
        assembly {
            return(0,0x20)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function returnTrue(string ) public
    {
        returnUint(1);
    }
    // function params type can not be correctly inferred, please check manually
    function emitTransfer(string from, string to, string amount) public
    {
        string signatureHash = 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef;
        emitEvent(signatureHash,from,to,amount);
    }
    // function params type can not be correctly inferred, please check manually
    function emitApproval(string from, string spender, string amount) public
    {
        string signatureHash = 0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925;
        emitEvent(signatureHash,from,spender,amount);
    }
    // function params type can not be correctly inferred, please check manually
    function emitEvent(string signatureHash, string indexed1, string indexed2, string nonIndexed) public
    {
        assembly {
            mstore(0,nonIndexed)
        }
        assembly {
            log3(0,0x20,signatureHash,indexed1,indexed2)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function ownerPos() public returns (string p)
    {
        p = 0;
    }
    // function params type can not be correctly inferred, please check manually
    function totalSupplyPos() public returns (string p)
    {
        p = 1;
    }
    // function params type can not be correctly inferred, please check manually
    function accountToStorageOffset(string account) public returns (string offset)
    {
        assembly {
            add(0x1000,account)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function allowanceStorageOffset(string account, string spender) public returns (string offset)
    {
        offset = accountToStorageOffset(account);
        assembly {
            mstore(0,offset)
        }
        assembly {
            mstore(0x20,spender)
        }
        assembly {
            keccak256(0,0x40)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function owner() public returns (string o)
    {
        assembly {
            sload(ownerPos())
        }
    }
    // function params type can not be correctly inferred, please check manually
    function totalSupply() public returns (string supply)
    {
        assembly {
            sload(totalSupplyPos())
        }
    }
    // function params type can not be correctly inferred, please check manually
    function mintTokens(string amount) public
    {
        assembly {
            sstore(totalSupplyPos(),safeAdd(totalSupply(),amount))
            totalSupplyPos()
            safeAdd(totalSupply(),amount)
            totalSupply()
        }
    }
    // function params type can not be correctly inferred, please check manually
    function balanceOf(string account) public returns (string bal)
    {
        assembly {
            sload(accountToStorageOffset(account))
        }
    }
    // function params type can not be correctly inferred, please check manually
    function addToBalance(string account, string amount) public
    {
        string offset = accountToStorageOffset(account);
        assembly {
            sstore(offset,safeAdd(sload(offset),amount))
            safeAdd(sload(offset),amount)
            sload(offset)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function deductFromBalance(string account, string amount) public
    {
        string offset = accountToStorageOffset(account);
        assembly {
            sload(offset)
        }
        require(lte(amount,bal));
        lte(amount,bal);
        assembly {
            sstore(offset,sub(bal,amount))
        }
    }
    // function params type can not be correctly inferred, please check manually
    function allowance(string account, string spender) public returns (string amount)
    {
        assembly {
            sload(allowanceStorageOffset(account,spender))
        }
    }
    // function params type can not be correctly inferred, please check manually
    function setAllowance(string account, string spender, string amount) public
    {
        assembly {
            sstore(allowanceStorageOffset(account,spender),amount)
            allowanceStorageOffset(account,spender)
        }
    }
    // function params type can not be correctly inferred, please check manually
    function decreaseAllowanceBy(string account, string spender, string amount) public
    {
        string offset = allowanceStorageOffset(account,spender);
        assembly {
            sload(offset)
        }
        require(lte(amount,currentAllowance));
        lte(amount,currentAllowance);
        assembly {
            sstore(offset,sub(currentAllowance,amount))
        }
    }
    // function params type can not be correctly inferred, please check manually
    function lte(string a, string b) public returns (string r)
    {
        assembly {
            iszero(gt(a,b))
        }
    }
    // function params type can not be correctly inferred, please check manually
    function gte(string a, string b) public returns (string r)
    {
        assembly {
            iszero(lt(a,b))
        }
    }
    // function params type can not be correctly inferred, please check manually
    function safeAdd(string a, string b) public returns (string r)
    {
        assembly {
            add(a,b)
        }
        if (or(lt(r,a),lt(r,b)))
        {
            assembly {
                revert(0,0)
            }
        }
    }
    // function params type can not be correctly inferred, please check manually
    function calledByOwner() public returns (string cbo)
    {
        assembly {
            eq(owner(),caller())
        }
    }
    // function params type can not be correctly inferred, please check manually
    function revertIfZeroAddress(string addr) public
    {
        require(addr);
    }
    // function params type can not be correctly inferred, please check manually
    function require(string condition) public
    {
        if (iszero(condition))
        {
            assembly {
                revert(0,0)
            }
        }
    }
}