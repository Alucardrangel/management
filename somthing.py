from dataclasses import dataclass

import os
properties_list = []
properties_dict = {}
tenant_list = []
tenant_dict = {}




@dataclass
class Manager:
  price: int
  address: str
  zipcode: str
  garage: str



@dataclass
class Tenant:
  name : str
  sex : str
  phone : int
  employed : bool
  email : str



  
well=('''                                                                                                                    
 _ _ _     _                      _          _____                     _          _____                        |  |
| | | |___| |___ ___ _____ ___   | |_ ___   |  _  |___ ___ ___ ___ ___| |_ _ _   |     |___ ___ ___ ___ ___ ___|  |
| | | | -_| |  _| . |     | -_|  |  _| . |  |   __|  _| . | . | -_|  _|  _| | |  | | | | .'|   | .'| . | -_|  _|__|
|_____|___|_|___|___|_|_|_|___|  |_| |___|  |__|  |_| |___|  _|___|_| |_| |_  |  |_|_|_|__,|_|_|__,|_  |___|_| |__|
                                                          |_|             |___|                    |___|           

''')


house_1=(''' 
           )
         ( _   _._
          |_|-'_~_`-._
       _.-'-_~_-~_-~-_`-._
   _.-'_~-_~-_-~-_~_~-_~-_`-._
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |  []  []   []   []  [] |______________.
    |           __    ___   |              |
  ._|  []  []  | .|  [___]  |              |._._._._._._._._._.
  |=|________()|__|()_______|       :      ||=|=|=|=|=|=|=|=|=|
^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    _______      ===
   <>              ===
      ^|^             ===
       |                 ===''')


house_2=(''' 
           )
         ( _   _._
          |_|-'_~_`-._
       _.-'-_~_-~_-~-_`-._
   _.-'_~-_~-_-~-_~_~-_~-_`-._
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |  []  []   []   []  [] |
    |           __    ___   |              
  ._|  []  []  | .|  [___]  |._._._._._._._._._._._._._._._._._.
  |=|________()|__|()_______||=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    _______      ===
   <_4rent_>       ===
      ^|^             ===
       |                 ===                        
                                        ______________________
                                       |,----.,----.,----.,--.\
                                       ||    ||    ||    ||   \\
                                       |`----'`----'|----||----\`.
                                       [    u-haul   |   -||- __|(|
                                       [  ,--.      |____||.--.  |
                                       =-(( `))-----------(( `))==
                                          `--'             `--'   ''')



big_house=('''

                          _______________________
            ____________.'                   .'\/`.
          .'       _  .' _______           .'\.'`./`.
        .'     _   _.'      _   _        .'\.' `._`./`.
      .' _       _.' __          __    .'\.'  ___`._`./`.
    .'        _ .'   _____           .'\.'         `._`./`.
  .'  _  _    .'       ______      .'\.'  __         `._`./`.
.'`--...__ _.'            ______ .'\.'           __    `._`./`.
 `--...__ .'   ____            .'\.'           _         `._`./`.
 |      .`--...__            .'\.'     _               ____`._`./`.
 | /`-._ `--...__`--...___ .'\.'              _______       _`._`./`.
 | | ) ( |       `--...____\.'     _     _  .'      .`.        `._`./
 | |)   (| /`-._             |            .'      .'   `.     _ |
 | |(--| | | )( |  /`-._`--._|____       /      .'       `.     |
 | | ) `.| |(  )|  | )( |    | _      _ /      /   .---.  `\    |
 | `--._ | |/  \|  |(  )|`-  |         /`--.._/   /     \  ' _  |
 | `-.   | |)-.(|  |/  \|    |       __|      |_  |`-   |  |  _ |
 |    `-.| |) |(|  |)-.(|    |  ___  _ |  __  | __| \`- |  |    |
 '-._    | `--._/  |) |(|    |      __ |      |   | |`- |  | _  |
     `-._| `--.    `--._/    |  ___    | _    |   | |`- |  |   '|
         |      `--._        |       _ |    ' |   |O|`- | _| _  |
         '--._         `--._ |         | _    |_ "| |`- |. |  __|
              `--._          |       __|      |   | |`- |. | __ |
                   `--._     |__       |   _  |"  | |`- |  |___ |
                        `--._|_________|_     | _ |  `- |_ |____|
                                         '--._|___|     |__|                               

                                                                                                                                                                                                                                          
                                                                    ______________________
                                                                   |,----.,----.,----.,--.\
                                                                   ||    ||    ||    ||   \\
                                                                   |`----'`----'|----||----\`.
                                                                   [    u-haul   |   -||- __|(|
                                                                   [  ,--.      |____||.--.  |
   <_4sale_>                                                       =-(( `))-----------(( `))==
      ^|^                                                             `--'             `--'
       |                              ''')




small_house=('''::::.
        _____A_
       /      /\\
    __/__/\__/  \___
---/__|" '' "| /___/\----
   |''|"'||'"| |' '||
   `""`""))""`"`""""`
                         <_4sale_>       
                            ^|^             
                             |  ''')




house_3=('''
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/\
          /  \    //_\       \    /\    \  /\/\/    \/    \
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \
 /\/\/\/       //_______\       \|__|      \
/      \      /XXXXXXXXXX\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~''')



Haunted_House=('''.     .
                               !!!!!!!
                       .       [[[|]]]    .
                       !!!!!!!!|--_--|!!!!!
                       [[[[[[[[\_(X)_/]]]]]
               .-.     /-_--__-/_--_-\-_--\
               |=|    /-_---__/__-__-_\__-_\
           . . |=| ._/-__-__\===========/-__\_
           !!!!!!!!!\========[ /]]|[[\ ]=====/
          /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
         /-_--_--_--_|=  === ||=/^|^\ ||== =|
        /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
       /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
      /-__--|_|_|_-_-| |_|_|=||______=||_| =|
     /_-__--_-__-___-|_=__=_.`---------'._=_|__
    /-----------------------\===========/-----/
   ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
       |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
       | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
       ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
       || == `||-----||' = ==|| | | |=|| |=||
       ||= == ||:^s^:|| = == ||=| | | || |=||
       || = = ||:___:||= == =|| |_|_| ||_|=||
      _||_ = =||o---.|| = ==_||_= == =||==_||_
      \__/= = ||:   :||= == \__/[][][][][]\__/
      [||]= ==||:___:|| = = [||]\\//\\//\\[||]
      }  {---'"'-----'"'- --}  {//\\//\\//}  {
    __[==]__________________[==]\\//\\//\\[==]_
   |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
   |^| ^  |================|^   | ^ ^^ ^ |  ^ ||
  \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
 \\///\\\//===============\\//\\///\\\\////\\\/////
 ""'""'""".'..'. ' '. ''..'.""'""'""'""''"''"''""    ''')


love_house=('''
                 
                             /^\
                    )       //^\\
                 (         //   \\
                   )      //     \\
                  __     //       \\
                 |=^|   //    _    \\
               __|= |__//    (+)    \\
              /LLLLLLL//      ~      \\
             /LLLLLLL//               \\
            /LLLLLLL//                 \\
           /LLLLLLL//  |~[|]~| |~[|]~|  \\
           ^| [|] //   | [|] | | [|] |   \\
            | [|] ^|   |_[|]_| |_[|]_|   |^
         ___|______|                     |
        /LLLLLLLLLL|_____________________|
       /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLL\
      /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLLLL\
      ^||^^^^^^^^/LLLLLLLLLLLLLLLLLLLLLLLLLL\
       || |~[|]~|^^||^^^^^^^^^^||^|~[|]~|^||^^
       || | [|] |  ||  |~~~~|  || | [|] | ||
       || |_[|]_|  ||  | [] |  || |_[|]_| ||
       ||__________||  |   o|  ||_________||
     .'||][][][][][||  | [] |  ||[][][][][||.'.
    ."'||[][][][][]||_-`----'-_||][][][][]||"."
  .(')^(.)(').( )'^@/-- -- - --\@( )'( ).(( )^(.)^
 '( )^(`)'.(').( )@/-- -- - -- -\@ (.)'(.),( ).(').
 ".'.'." ." '.". @/- - --- -- - -\@ '.".'.".'.".'."
 ". '' ".".".'.'@/ - -- -- -- -- -\@".'..'".'."'.'.'
'.".".''.".''."@/ -- --- --- -- - -\@.".''.".''.".'".''')


apt_house=('''                                (
            (                                 )
    ________[]_                              []
   /^=^-^-^=^-^\                   /^~^~^~^~^~^~\
  /^-^-^-^-^-^-^\                 /^ ^ ^  ^ ^ ^ ^\
 /__^_^_^_^^_^_^_\               /_^_^_^^_^_^_^_^_\
  |  .==.       |       ___       |        .--.  |
^^|  |LI|  [}{] |^^^^^ /___\ ^^^^^|  [}{]  |[]|  |^^^^^
&&|__|__|_______|&&   ." | ".   88|________|__|__|888
     ====             (o_|_o)              ====
      ====             u   u              ====''')


pictures = (well, house_1, house_2, big_house, small_house, house_3)



def view_tenant_info():
  tenant_response = input("Search for tenants by [sex] [name] or [job status] > ")
  for name in tenant_list:
    if tenant_response == "sex":
      select_gender = input("[male] or [female] > ")
      if select_gender == "male" and name.sex == "male":
        print(f"Here are your male tenants! {name.name}")
      elif select_gender == "female" and name.sex == "female":
        print(f"Here are your female tenants! {name.name}")
      else:
        print("You have no tenants. Make sure you have some to search through first!")
    elif tenant_response == "name":
      which_person = input("Who are you looking for? > ")
      if which_person == name.name:
        print(f"{which_person} is a tenant! Their contact information is Phone: {name.phone} and Email: {name.email}")
      else:
        print("This person is not a active tenant.")
    elif tenant_response == "job status":
      if name.employed == True:
        print(f"{name.name}: Employed")
      else:
        print(f"{name.name}: Unemployed")
    else:
      print("Please select a valid input")
        



def check_in_visitor():
    which_person = input("Who do you want to visit? > ")
    tenant_list = os.listdir('tenants')
    for name in tenant_list:
      if which_person == name.replace('.txt', ''):
        guest_name = input("Add your name to our check in list > ")
        with open(f'tenants/{name}', 'a') as file:
          file.write(f'\n{guest_name} is visiting')
        
      else:
        print("This person doesn't live here!")
    

def view_all_tenants():
  list = os.listdir('tenants')
  for tenant in list:
    with open(f'tenants/{tenant}', 'r') as file:
      print(f"- {file.read()}")
   
     
    
def add_tenant():
    address_list = os.listdir('properties')
    home_selection = input("What home is this tenant staying in (address)? > ")
    for property in address_list:
      prop = property.replace('.txt', '')
      if home_selection == prop:
        name = input("What is the name of the tenant? > ")
        sex = input("What is the sex of the tenant? > ")
        phone = int(input("Tenants phone number? > "))
        employed = input("Is the tenant employed? > ")
        email = input("Tenants' email > ")
        print(f"{Haunted_House}")

        if employed == "yes":
          tenant_list.append(Tenant(name, sex, phone, True, email))
        else:
          tenant_list.append(Tenant(name, sex, phone, False, email))
        for tenant in tenant_list:
          if tenant == tenant_list.pop():
            tenant_dict[f'{tenant.name}'] = tenant
            with open(f"properties/{prop}.txt", 'a') as file:
              file.writelines(f'\n{tenant.name} lives here')
            with open(f'tenants/{tenant.name}.txt', 'w') as file:
                file.write(f'{tenant}')
            with open(f'tenants/{tenant.name}.txt', 'a') as file:
              file.writelines(f'\nLives at {prop}')


def view_all_properties():
  list = os.listdir('properties')
  for property in list:
    with open(f'properties/{property}') as file:
      print(f"- {file.read()}")


def buy_a_home():
    address = input("What is the address of the home? > ")
    price = int(input("What is the price of this home? > "))
    zipcode = input("What is the zipcode of where the home is located? > ")
    garage = input("Does this property have a garage? > ")
   
  
    properties_list.append(Manager(price, address, zipcode, garage))
    open(f'properties/{address}.txt', 'w')
    for property in properties_list:
      if property == properties_list.pop():
        properties_dict[f'{property.address}'] = property
        with open(f'properties/{address}.txt', 'a') as file:
          file.write(f'{property}')
    
    
  
    
    
    
def property_search():
    user_selection = input("Enter a perameter to search through your homes such as [pool], [garage], or [zipcode]. >  ")
    for property in properties_list:
      if user_selection == "garage":
        which_home2 = input("Which home do you want to see has a garage? > ")
        if which_home2 == property.address and property.garage == "yes":
          print(f"This address features a Garage!\n{house_1}")
          
        else:
          print("This house does not have a Garage.")
      elif user_selection == "zipcode":
        which_home3 = input("Which home do you want to check what zipcode they're in? > ")
        if which_home3 == property.address:
          print(f"This home is located in {property.zipcode}.")
        else:
          print("Invalid address.")






def main():
  print(f"{well} Please select a option ")
  
  while True:
    user_input = input("[buy] a home [search] my homes, [new lease], pay a [visit] to someone, [view tenant info], view [all properties], view [all tenants], or [quit] > ")
    if user_input == 'quit':
      break
    elif user_input == "buy":
      buy_a_home()
    elif user_input == "search":
      property_search()
    elif user_input == "new lease":
      add_tenant()
    elif user_input == "view tenant info":
      view_tenant_info()
    elif user_input == "visit":
      check_in_visitor()
    elif user_input == 'all properties':
      view_all_properties()
    elif user_input == 'all tenants':
      view_all_tenants()
    else:
      print('invalid action')

if __name__ == '__main__':
  main()