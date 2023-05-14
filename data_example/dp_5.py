import pandas as pd
import perfplot

def concat_loop(lst):
    df = pd.DataFrame(columns=['A', 'B'])
    for dic in lst:
        df = pd.concat([df, pd.DataFrame([dic])], ignore_index=True)
    return df.infer_objects()
    
def concat_once(lst):
    df = pd.DataFrame(columns=['A', 'B'])
    df = pd.concat([df, pd.DataFrame(lst)], ignore_index=True)
    return df.infer_objects()

def loc_loop(lst):
    df = pd.DataFrame(columns=['A', 'B'])
    for dic in lst:
        df.loc[len(df)] = dic
    return df


perfplot.plot(
    setup=lambda n: [{'A': i, 'B': 'a'*(i%5+1)} for i in range(n)],
    kernels=[concat_loop, concat_once, loc_loop],
    labels= ['concat in a loop', 'concat once', 'loc in a loop'],
    n_range=[2**k for k in range(16)],
    xlabel='Length of dataframe',
    title='Enlarging a dataframe in a loop',
    relative_to=1,
    equality_check=pd.DataFrame.equals);
