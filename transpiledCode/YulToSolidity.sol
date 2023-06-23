pragma solidity >=0.4.22 <0.9.0;


contract CrowdFunding
{
     constructor() public
    {
        //datacopy(0x00,dataoffset("runtime"),datasize("runtime")) function datacopy not declared
        //dataoffset("runtime") function dataoffset not declared
        //datasize("runtime") function datasize not declared
        assembly {
            return(0x00,datasize("runtime"))
            //datasize("runtime") function datasize not declared
        }
    }
}
function runtime() public
{
    if (selector() == 0x22502268)
    {
        checkParamLenght(2);
        assembly {
            sload(0x00)
        }
        assembly {
            mstore(0x00,id)
        }
        assembly {
            keccak256(0x00,0x20)
        }
        assembly {
            sstore(structSlot,caller())
        }
        assembly {
            sstore(add(structSlot,0x20),calldataload(4))
        }
        assembly {
            sstore(add(structSlot,0x40),add(timestamp(),calldataload(36)))
        }
        assembly {
            sstore(0x00,add(id,1))
        }
    }
    else if (selector() == 0xc1cbbca7)
    {
        checkParamLenght(1);
        assembly {
            require(lt(0,callvalue()))
        }
        assembly {
            calldataload(4)
        }
        assembly {
            mstore(0x00,id)
        }
        assembly {
            keccak256(0x00,0x20)
        }
        assembly {
            sload(add(campaignStructSlot,0x40))
        }
        assembly {
            require(lt(timestamp(),endTimestamp))
        }
        assembly {
            mstore(0x20,caller())
        }
        assembly {
            keccak256(0x00,0x40)
        }
        assembly {
            sload(storageSlot)
        }
        assembly {
            sstore(storageSlot,add(alreadyInvested,callvalue()))
        }
        assembly {
            add(campaignStructSlot,0x60)
        }
        assembly {
            sload(totalStorageSlot)
        }
        assembly {
            sstore(totalStorageSlot,add(previousTotal,callvalue()))
        }
    }
    else if (selector() == 0x6ef98b21)
    {
        checkParamLenght(1);
        assembly {
            mstore(0x00,calldataload(4))
        }
        assembly {
            keccak256(0x00,0x20)
        }
        assembly {
            add(ownerStorageSlot,0x20)
        }
        assembly {
            add(ownerStorageSlot,0x40)
        }
        assembly {
            add(ownerStorageSlot,0x60)
        }
        assembly {
            sload(amountRaisedSlot)
        }
        assembly {
            require(eq(caller(),sload(ownerStorageSlot)))
        }
        assembly {
            require(lt(sload(targetAmountSlot),amountRaised))
        }
        assembly {
            sstore(amountRaisedSlot,0)
        }
        assembly {
            sstore(endTimestampSlot,sub(0,1))
        }
        assembly {
            if iszero(call(gas(),caller(),amountRaised,0,0,0,0))
            {
                revert(0,0)
            }
        }
    }
    else if (selector() == 0x152b58ab)
    {
        checkParamLenght(1);
        assembly {
            mstore(0x00,calldataload(4))
        }
        assembly {
            keccak256(0x00,0x20)
        }
        assembly {
            add(ownerStorageSlot,0x20)
        }
        assembly {
            add(ownerStorageSlot,0x40)
        }
        assembly {
            add(ownerStorageSlot,0x60)
        }
        assembly {
            require(lt(sload(endTimestampSlot),timestamp()))
        }
        assembly {
            require(lt(sload(amountRaisedSlot),sload(targetAmountSlot)))
        }
        assembly {
            mstore(0x20,caller())
        }
        assembly {
            keccak256(0x00,0x40)
        }
        assembly {
            sload(storageSlot)
        }
        assembly {
            require(lt(0,amountToSend))
        }
        assembly {
            sstore(storageSlot,0)
        }
        transfer(amountToSend);
    }
    else
    {
        assembly {
            revert(0,0)
        }
    }
}
// function params type can not be correctly inferred, please check manually
function selector() public returns (uint256 s)
{
    assembly {
        s:=div(calldataload(0),0x100000000000000000000000000000000000000000000000000000000)
    }
}
// function params type can not be correctly inferred, please check manually
function require(uint256 condition) public
{
    assembly {
        if iszero(condition)
        {
            revert(0,0)
        }
    }
}
// function params type can not be correctly inferred, please check manually
function checkParamLenght(uint256 len) public
{
    assembly {
        require(eq(calldatasize(),add(4,mul(32,len))))
    }
}
// function params type can not be correctly inferred, please check manually
function transfer(uint256 amount) public
{
    assembly {
        if iszero(call(gas(),caller(),amount,0,0,0,0))
        {
            revert(0,0)
        }
    }
}