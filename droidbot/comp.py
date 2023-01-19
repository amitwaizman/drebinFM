import json,sys,os

#compare a state
def comp_state(s1,s2):
        names=s1==s2#state compare
        forg_names=s1[0]==s2[0]#forground activities
        act_names=s1[1]==s2[1]#activities
        return names,forg_names,act_names


#compare all the states
def comp_states(s1,s2):
        s1=list(s1.keys())
        s2=list(s2.keys())
        if len(s1)!=len(s2):#not equal number of states
                return False
        s=0
        for i in range(len(s1)):
                s+=not(comp_state(s1[i],s2[i]))
        return s


#compare a state
def comp_event(s1,s2):
        names=s1==s2#state compare
        start_state=s1[0]==s2[0]#forground activities
        stop_state=s1[1]==s2[1]#forground activities
        event_info=s1[2]==s2[2]#forground activities
        return names,start_state,stop_state,event_info


#compare all the events
def comp_events(s1,s2):
        st1=s1
        st2=s2
        s1=list(s1.keys())
        s2=list(s2.keys())
        if len(s1)!=len(s2):#not equal number of states
                return False
        s=0
        try:
                for i in range(len(s1)):
                        s+=not(comp_state(s1[i],s2[i]))
        except Exception as e:
                print(st1,st2)
                print(e)
                exit(0)
        return s



#generate the chain
def gen_chain_compare(states,events):
        inconsist_list=[]
        try:
                s0,e0=states[0],events[0]
                if not s0 or not e0:
                        return [-1,-1]
        except Exception as e:
                print(e)
        truth_s=0
        truth_e=0
        #compare states
        for s in states[1:]:
                truth_s+=comp_states(s0,s)
        #compare states
        for e in events[1:]:
                truth_e+=comp_events(s0,s)
        return [truth_s,truth_e]
#create chain func
def create_data(f):
       ev_folder=f+os.path.sep+"events"
       st_folder=f+os.path.sep+"states"
       if not(os.path.isdir(ev_folder)) or not(os.path.isdir(st_folder)):
        return [],[]
       events_files=[ev_folder+os.path.sep+x for x in os.listdir(f+os.path.sep+"events")] 
       states_files=[st_folder+os.path.sep+x for x in os.listdir(f+os.path.sep+"states") if not(x.endswith(".png"))]
       events_files.sort()
       states_files.sort()
       states_list={}
       events_list={}
       #states files
       for s in states_files:
                try:
                        data=open(s,'r').read()
                        if not data:
                                continue
                        state=json.loads(data)
                        if not state:
                                continue
                        #important info to remember
                        name=state['state_str']
                        forg_act=state['foreground_activity']
                        act_stack=state['activity_stack']
                        serv=state['background_services']
                        wid=state['width']
                        hei=state['height']
                        views=state['views']
                        states_list[name]=[forg_act,act_stack,serv,wid,hei,views]
                except Exception as e:
                        print(states_files,e)
       #events files
       for et in events_files:
                try:
                        data=open(et,'r').read()
                        if not data:
                                continue
                        event=json.loads(data)
                        
                        #important info to remember
                        name=event["event_str"].split("(")[0]
                        start_state=event["start_state"]
                        stop_state=event["stop_state"]
                        event_info=event["event"]
                        events_list[name]=[start_state,stop_state,event_info]
                except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                        print(event)
                        print(open(et,'r').read())
                        
       return states_list,events_list
  

#this script uses a result file to document the different states/events
#in droidbot, for functionality assesment
#the input is the path of outputs of droidbot
#the former and manipulated apps should use the same name
#	
path=sys.argv[1]
files=os.listdir(path)
dict_files={}
for f in files:
        name=f.split("_")[0]
        if name in dict_files.keys():
                dict_files[name].append(f)
        else:
                dict_files[name]=[f]
print(dict_files)





res_file=open("/home/rivka/Desktop/labDDOS/droidbot/result/result.txt","w")
#run the keys
for k in dict_files.keys():
      #former app
      files=dict_files[k]
      files.sort()
      #store the data
      states=[]
      events=[]
      flaw=0
      try:
              for f in files:
                try:
                        s,e=create_data(path+os.path.sep+f)
                        if not(s) or not(e):
                                res_file.write(k+",-1,-1\n")
                                flaw=1
                                break        
                        states.append(s)
                        events.append(e)
                except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                        if "No such file or directory" in str(e):
                                continue
                        else:
                                print(e,k)
              if flaw==0:
                      results=gen_chain_compare(states,events)
                      res_file.write(k+","+str(results[0])+","+str(results[1])+"\n")
              else:
                      flaw=0
      except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                        print(e,k)
                        continue
